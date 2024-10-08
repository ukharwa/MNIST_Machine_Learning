import os
from KNN import KNN

train_file = open(os.getcwd() + "/data/train.csv", "r")
train_list = train_file.readlines()
train_file.close()

test_file = open(os.getcwd() + "/data/test.csv", "r")
test_list = test_file.readlines()
test_file.close()

knn = KNN(train_list, 3)
print(knn.accuracy(test_list[0:10]))