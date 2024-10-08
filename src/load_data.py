import os;

def convert(imgs, labels, labels_outfile, data_outfile, n):  #converts from ubyte to csv
    imgf = open(imgs, "rb")
    labelf = open(labels, "rb")
    csvf = open(data_outfile, "w")
    lcsvf = open(labels_outfile, "w")

    imgf.read(16)
    labelf.read(8)
    images = []

    for i in range(n):
        image = []
        for j in range(28*28):
            image.append(ord(imgf.read(1)))
        images.append(image)

    for i in range(n):
        lcsvf.write(str(ord(labelf.read(1))) + "\n")

    for image in images:
        csvf.write(",".join(str(pix) for pix in image) + "\n")
    
    imgf.close()
    labelf.close()
    csvf.close()
    lcsvf.close()


mnist_train_x = os.getcwd() + "/data/train-images-idx3-ubyte"
mnist_train_y = os.getcwd() + "/data/train-labels-idx1-ubyte"

mnist_test_x = os.getcwd() + "/data/t10k-images-idx3-ubyte"
mnist_test_y = os.getcwd() + "/data/t10k-labels-idx1-ubyte"

#convert(mnist_train_x, mnist_train_y, os.getcwd() + "/data/Y_train.csv", os.getcwd() + "/data/X_train.csv", 60000)
convert(mnist_test_x, mnist_test_y, os.getcwd() + "/data/Y_test.csv", os.getcwd() + "/data/X_test.csv", 10000)
