import numpy as np
from collections import Counter
import time

class KNN:
    def __init__(self, x_train, y_train, k):
        self.k = k
        self.y_train = y_train
        self.x_train = []
        for i in x_train:
            self.x_train.append(i.split(","))
        

    def euclidean_distance(self, train_data, test_data):
        return np.sqrt(np.sum((np.asarray(train_data, dtype=float) - np.asarray(test_data, dtype=float))**2))

    def predict(self, x):
        distances = [self.euclidean_distance(i, x.split(",")) for i in self.x_train]

        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        return Counter(k_nearest_labels).most_common()[0][0]
        

    def accuracy(self, x_test, y_test):
        start =  time.time()
        predictions = [self.predict(i) for i in x_test]
        print(time.time() - start)
        return (np.sum(np.asarray(predictions) == np.asarray(y_test)) / len(y_test)) * 100