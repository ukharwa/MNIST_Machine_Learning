from DNN_class_abstraction import DNN
import numpy as np

pred_file = open("pred.csv", "r")
pred_list = pred_file.readlines()
pred_file.close()

def line_split(line):
    return line.strip().split(",")

pred_list = list(map(line_split, pred_list))

dnn = DNN([784, 500, 200, 100, 10], "weights4.txt")
dnn.predict(pred_list)