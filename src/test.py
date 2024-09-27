
import numpy as np

weights_file = open("weights.txt", "r")
weight_lines = weights_file.readlines()
weights_file.close()

arr_weights = []
for line in weight_lines:
    arr_weights.append(list(map(float, line.strip().split(","))))

w1 = np.asarray(arr_weights[0]).reshape(128,784)
w2 = np.asarray(arr_weights[1]).reshape(64,128)
w3 = np.asarray(arr_weights[2]).reshape(10,64)

print(len(w1[0]))
print(len(w2[0]))
print(len(w3[0]))