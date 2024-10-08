from DNN_class import DNN
import numpy as np
import os

pred_file = open(os.getcwd() + "/pred.csv", "r")
pred_list = pred_file.readlines()
pred_file.close()

weights_file = open(os.getcwd() + "/weights1.txt", "r")
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

dnn = DNN([784, 128, 64, 10], starting_weights)
dnn.predict(pred_list[0])