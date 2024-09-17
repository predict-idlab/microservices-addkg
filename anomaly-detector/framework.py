from sklearn.neighbors import LocalOutlierFactor
from adtk.detector import OutlierDetector
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn.utils.class_weight import compute_class_weight
import numpy as np
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from adtk.detector import ThresholdAD


class Framework:
    def __init__(self, models, train_range, test_range, validation_strategy):
        self.models = models
        self.train_range = train_range
        self.test_range = test_range
        self.val_strategy = validation_strategy
        
    def evaluate(self):
        results = {}
        for name, model in self.models.items():
            model.optimize(self.train_range, self.val_strategy)
            model.score(self.test_range)
            results[name] = model.stats(self.test_range)
        return results


class GenericModel:
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
        self.y_pred = None

    def optimize(self, train_range, strategy=None):
        raise NotImplementedError

    def score(self, test_range):
        if self.y_pred is None:
            raise NotImplementedError
        
    def stats(self, test_range):
        result = {}
        y_true = self.labels[(self.labels.index>test_range[0]) & (self.labels.index<test_range[1])]
        result["Accuracy"] = accuracy_score(y_true, self.y_pred)
        result["Precision"] = precision_score(y_true, self.y_pred)
        result["Recall"] = recall_score(y_true, self.y_pred)
        result["F1"] = f1_score(y_true, self.y_pred)
        result["Weighted F1"] = f1_score(y_true, self.y_pred, average="weighted")
        return result


class DeucalionOutlierDetection(GenericModel):
    def optimize(self, train_range, strategy=None):
        X_train = self.data[(self.data.index>=train_range[0]) & (self.data.index<=train_range[1])]
        y_train = self.labels[(self.labels.index>=train_range[0]) & (self.labels.index<=train_range[1])]
        if strategy is None:
            self.model = OutlierDetector(LocalOutlierFactor())
        else:
            current_best_score = 0
            current_best = None
            for n in [10,20,30,40, 50, 75, 100, 120, 200, 500]:
                model = OutlierDetector(LocalOutlierFactor(n_neighbors=n))
                anomalies = model.fit_detect(X_train).fillna(False)
                print(n,f1_score(y_train, anomalies))
                if f1_score(y_train, anomalies)>current_best_score:
                    current_best_score=f1_score(y_train, anomalies)
                    current_best = model
            if current_best is not None:
                self.model = current_best
            else:
                self.model = OutlierDetector(LocalOutlierFactor())

    def score(self, test_range):
        X_test = self.data[(self.data.index>test_range[0]) & (self.data.index<test_range[1])]
        self.y_pred = self.model.fit_detect(X_test).fillna(False)


class DeucalionLevelDetection(GenericModel):
    def optimize(self, train_range, strategy=None):
        X_train = self.data[(self.data.index>=train_range[0]) & (self.data.index<=train_range[1])]
        y_train = self.labels[(self.labels.index>=train_range[0]) & (self.labels.index<=train_range[1])]
        if strategy is None:
            self.model = ThresholdAD(high=0.01, low=0)
        else:
            current_best_score = 0
            current_best = None
            for n in np.arange(0.01, 0.1, 0.01):
                model = ThresholdAD(high=n, low=0)
                anomalies = model.detect(X_train).fillna(False)
                print(n,f1_score(y_train, anomalies))
                if f1_score(y_train, anomalies)>current_best_score:
                    current_best_score=f1_score(y_train, anomalies)
                    current_best = model
            if current_best is not None:
                self.model = current_best
            else:
                self.model = ThresholdAD(high=0.01, low=0)
            

    def score(self, test_range):
        X_test = self.data[(self.data.index>test_range[0]) & (self.data.index<test_range[1])]
        self.y_pred = self.model.detect(X_test).fillna(False)

class DeucalionSupervisedDetection(GenericModel):    
    def optimize(self, train_range, strategy=None):
        X_train = self.data[(self.data.index>=train_range[0]) & (self.data.index<=train_range[1])]
        y_train = self.labels[(self.labels.index>=train_range[0]) & (self.labels.index<=train_range[1])]
        
        #self.scaler = MinMaxScaler()
        #X_train_scaled = self.scaler.fit_transform(X_train.fillna(-1)) ## might introduce issues

        class_weights = compute_class_weight(class_weight="balanced", classes=np.unique(y_train), y=y_train)
        class_labels = sorted(set(y_train))
        class_weights_dict = dict(zip(class_labels, class_weights))
        
        if strategy is None:
            #self.model = SVC(kernel='rbf', class_weight=class_weights_dict, random_state=42)
            self.model = RandomForestClassifier()
            self.model.fit(X_train, y_train)
        
        else:
            param_grid = {
                'n_estimators' : [1, 5, 10,50,100,250,500],
                'class_weight': [class_weights_dict]
            }
            grid_search = GridSearchCV(estimator=RandomForestClassifier(), param_grid=param_grid, cv=strategy, scoring='f1')
            #grid_search.fit(X_train_scaled, y_train)
            grid_search.fit(X_train, y_train)
            
            best_params = grid_search.best_params_
            print("Best Parameters:", best_params)

            self.model = grid_search.best_estimator_
            self.model.fit(X_train, y_train)
            

    def score(self, test_range):
        X_test = self.data[(self.data.index>test_range[0]) & (self.data.index<test_range[1])]
        #X_test_scaled = self.scaler.fit_transform(X_test.fillna(-1)) ## might introduce issues
        self.y_pred = self.model.predict(X_test)