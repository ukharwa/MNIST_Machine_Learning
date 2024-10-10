import numpy as np
import matplotlib.pyplot as plt

train_file = open("/home/ukharwa/MNIST/data/X_train.csv", "r")
train_list = train_file.readlines()
train_file.close()

values = train_list[1].split(",")
image_array = np.asarray(values, dtype=float).reshape((28, 28))
plt.imshow(image_array, cmap="Greys", interpolation="None")
plt.show()