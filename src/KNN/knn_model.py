import os
from KNN import KNN

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

#pred_file = open(os.getcwd() + "/pred.csv", "r")
#pred_list = pred_file.readlines()
#pred_file.close()

knn = KNN(x_train, y_train, 3)
print(knn.predict(x_test[0]))