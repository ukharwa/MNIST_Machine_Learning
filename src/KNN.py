import numpy as np
from collections import Counter

class KNN:
    def __init__(self, train_data, k):
        self.k = k
        self.train_data = []
        for i in train_data:
            self.train_data.append(i.split(","))

    def euclidean_distance(self, train_data, test_data):
        return np.sqrt(np.sum((np.asarray(train_data, dtype=float) - np.asarray(test_data, dtype=float))**2))

    def predict(self, x):
        distances = [self.euclidean_distance(x, i[1:]) for i in self.train_data[0:1000]]

        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.train_data[i][0] for i in k_indices]

        return Counter(k_nearest_labels).most_common()[0][0]
        

    def accuracy(self, test_data):
        predictions = [self.predict(i.split(",")[1:]) for i in test_data]
        print(predictions)
        y_test = [i.split(",")[0] for i in test_data]
        print(y_test)
        return (np.sum(np.asarray(predictions) == np.asarray(y_test)) / len(y_test)) * 100