
from DNN_class_abstraction import DNN
import os
import numpy as np

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

#values = x_train[0].split(",")
#inputs = (np.asarray(values, dtype=float) / 255.0 * 0.99) + 0.01

def line_split(line):
    return line.strip().split(",")


x_test = list(map(line_split, x_test))
x_train = list(map(line_split, x_train))

dnn = DNN([784, 500, 200, 100, 10], "weights4.txt")
dnn.train(x_train, y_train, x_test, y_test, 50, 0.5)