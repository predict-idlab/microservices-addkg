from sklearn.metrics import accuracy_score, precision_score, recall_score


def print_stats(predictions, labels_):
    print("Accuracy = {}".format(accuracy_score(labels_, predictions)))
    print("Precision = {}".format(precision_score(labels_, predictions)))
    print("Recall = {}".format(recall_score(labels_, predictions)))
