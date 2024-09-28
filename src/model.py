
from DNN_class import DNN
import numpy as np

# create lists of the training and testing data
train_file = open("/home/ukharwa/MNIST/data/train.csv", "r")
train_list = train_file.readlines()
train_file.close()
test_file = open("/home/ukharwa/MNIST/data/test.csv", "r")
test_list = test_file.readlines()
test_file.close()
pred_file = open("/home/ukharwa/MNIST/pred.csv", "r")
pred_list = pred_file.readlines()
pred_file.close()

weights_file = open("/home/ukharwa/MNIST/weights.txt", "r")
weight_lines = weights_file.readlines()
weights_file.close()

arr_weights = []
for line in weight_lines:
    arr_weights.append(list(map(float, line.strip().split(","))))

w1 = np.asarray(arr_weights[0]).reshape(128,784)
w2 = np.asarray(arr_weights[1]).reshape(64,128)
w3 = np.asarray(arr_weights[2]).reshape(10,64)
acc = arr_weights[3]

starting_weights = [w1, w2, w3, acc]


dnn = DNN(starting_weights)
#print(dnn.compute_accuracy(test_list) * 100)
dnn.predict(pred_list)