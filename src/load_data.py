import os;

def convert(imgs, labels, outfile, n):  #converts from ubyte to csv
    imgf = open(imgs, "rb")
    labelf = open(labels, "rb")
    csvf = open(outfile, "w")

    imgf.read(16)
    labelf.read(8)
    images = []

    for i in range(n):
        image = [ord(labelf.read(1))]
        for j in range(28*28):
            image.append(ord(imgf.read(1)))
        images.append(image)

    for image in images:
        csvf.write(",".join(str(pix) for pix in image) + "\n")
    
    imgf.close()
    labelf.close()
    csvf.close()


mnist_train_x = os.getcwd() + "/data/train-images-idx3-ubyte"
mnist_train_y = os.getcwd() + "/data/train-labels-idx1-ubyte"

mnist_test_x = os.getcwd() + "/data/t10k-images-idx3-ubyte"
mnist_test_y = os.getcwd() + "/data/t10k-labels-idx1-ubyte"

convert(mnist_train_x, mnist_train_y, os.getcwd() + "/data/train.csv", 60000)
convert(mnist_test_x, mnist_test_y, os.getcwd() + "/data/test.csv", 10000)
