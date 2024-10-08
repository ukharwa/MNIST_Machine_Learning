
from DNN_class import DNN
import os

#create lists of the training and testing data
train_file = open(os.getcwd() + "/data/X_train.csv", "r")
x_train = train_file.readlines()
train_file.close()
train_file = open(os.getcwd() + "/data/Y_train.csv", "r")
y_train = train_file.readlines()
train_file.close()

test_file = open(os.getcwd() + "/data/X_test.csv", "r")
x_test = test_file.readlines()
test_file.close()
test_file = open(os.getcwd() + "/data/Y_test.csv", "r")
y_test = test_file.readlines()
test_file.close()

weights_file = open(os.getcwd() + "/weights2.txt", "r")

dnn = DNN([784, 392, 128, 10], "weights2.txt")
dnn.train(x_train, y_train, x_test, y_test, 2, 0.5)