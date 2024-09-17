import numpy as np
import pandas as pd


def temporalize(X, y, window_size=5):

    output_X = []
    output_y = []
    for i in range(len(X) - window_size):
        output_X.append(X[i:i + window_size])
        output_y.append(y[i + window_size])

    return np.array(output_X), np.array(output_y)


def evaluate(true_regions, predicted_timestamps, false_pos_region_delta=None):
    true_positives = 0
    false_positives = 0
    total_positives = 0

    found_true_positive = set()
    found_false_positive = set()
    # Iterate over each predicted timestamp
    for timestamp in predicted_timestamps:
        timestamp_found = False
        # Iterate over each true window
        for true_start, true_end in true_regions:
            # Check if the predicted timestamp falls within the current true window
            if true_start <= timestamp <= true_end:
                # If it falls within the window and a true positive within the window was already found ,
                # just continue, these predictions are related and close to each other
                if (true_start, true_end) in found_true_positive:
                    timestamp_found = True
                    break
                # If it falls within the window and a true positive within the window is not found yet,
                # count it as a true positive and set the flag to True
                true_positives += 1
                found_true_positive.add((true_start, true_end))
                timestamp_found = True
                break
        # If the predicted timestamp falls outside the window, count it as a false positive
        if not timestamp_found:
            # but check if a previous false positive was within the range of an already detected false positive
            in_region = False
            for region in found_false_positive:
                if region[0] <= timestamp <= region[1]:
                    #if so, we just neglect it
                    in_region = True
                    break
            if not in_region:
                # otherwise, we add it, together with its range
                false_positives += 1
                if false_pos_region_delta is not None:
                    found_false_positive.add((timestamp, timestamp+false_pos_region_delta))


    # Calculate total number of true positives
    total_positives = len(true_regions)

    # Calculate precision and recall
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) != 0 else 0
    recall = true_positives / total_positives if total_positives != 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
    return precision, recall, f1


class RealTimePeakDetector:
    def __init__(self, df: pd.DataFrame, lag: int, threshold, influence):
        self.y = df
        self.length = len(self.y)
        self.lag = lag
        self.threshold = threshold
        self.influence = influence
        self.signals = [0] * len(self.y)
        self.filteredY = np.array(self.y)
        self.avgFilter = [0] * len(self.y)
        self.stdFilter = [0] * len(self.y)
        self.avgFilter[self.lag - 1] = self.y[:self.lag].mean()
        self.stdFilter[self.lag - 1] = self.y[:self.lag].std()

        # mean = df.mean()
        # std = df.std()
        #
        # z_scores = abs((df - mean) / std)
        # z_scores = z_scores.mean(axis=1)
        # df[SCORE] = z_scores

    def thresholding_algo(self, new_value):
        self.y.append(new_value)
        i = len(self.y) - 1
        self.length = len(self.y)
        if i < self.lag:
            return 0
        elif i == self.lag:
            self.signals = [0] * len(self.y)
            self.filteredY = np.array(self.y)
            self.avgFilter = [0] * len(self.y)
            self.stdFilter = [0] * len(self.y)
            self.avgFilter[self.lag] = self.y[:self.lag].mean()
            self.stdFilter[self.lag] = self.y[:self.lag].std()
            return 0

        self.signals += [0]
        self.filteredY += [0]
        self.avgFilter += [0]
        self.stdFilter += [0]

        if abs(self.y[i] - self.avgFilter[i - 1]) > (self.threshold * self.stdFilter[i - 1]):

            if self.y[i] > self.avgFilter[i - 1]:
                self.signals[i] = 1
            else:
                self.signals[i] = -1

            self.filteredY[i] = self.influence * self.y[i] + \
                (1 - self.influence) * self.filteredY[i - 1]
            self.avgFilter[i] = np.mean(self.filteredY[(i - self.lag):i])
            self.stdFilter[i] = np.std(self.filteredY[(i - self.lag):i])
        else:
            self.signals[i] = 0
            self.filteredY[i] = self.y[i]
            self.avgFilter[i] = np.mean(self.filteredY[(i - self.lag):i])
            self.stdFilter[i] = np.std(self.filteredY[(i - self.lag):i])

        return self.signals[i]
