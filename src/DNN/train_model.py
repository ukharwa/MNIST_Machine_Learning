
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

dnn = DNN([784, 128, 64, 10], "weights3.txt")
#print(dnn.forward_pass(inputs))
dnn.train(x_train, y_train, x_test, y_test, 10, 0.05)