
import numpy as np
import time

# creat dense neural network object
class DNN:
    def __init__(self, size, weightsFile):
        try:
            weights_file = open(weightsFile, "r")
            weight_lines = weights_file.readlines()
            weights_file.close()

            arr_weights = []
            for line in weight_lines:
                arr_weights.append(list(map(float, line.strip().split(","))))
            
            input_layer = size[0]
            hidden_layer_1 = size[1]
            hidden_layer_2 = size[2]
            output_layer = size[3]

            self.accuracy = arr_weights[3][0]
            self.params = {
                "w1": np.asarray(arr_weights[0]).reshape(hidden_layer_1,input_layer),
                "w2": np.asarray(arr_weights[1]).reshape(hidden_layer_2,hidden_layer_1),
                "w3": np.asarray(arr_weights[2]).reshape(output_layer,hidden_layer_2)
            }

        except Exception as error:
            print(error)
            print("No starting weights found. Generating random values")
            self.accuracy = 0
            # set layer sizes
            input_layer = size[0]
            hidden_layer_1 = size[1]
            hidden_layer_2 = size[2]
            output_layer = size[3]

            # setting random weights for the connections between each pair of layers
            # np.random.randn(x, y) generates an array of dimensions x*y with random numbers from the normal distribution
            # we multiply that by np.sqrt(1./x) which normalises the matrix (scales the values nicely somehow)
            self.params = {
                "w1": np.random.randn(hidden_layer_1, input_layer) * np.sqrt(1./hidden_layer_1),
                "w2": np.random.randn(hidden_layer_2, hidden_layer_1) * np.sqrt(1./hidden_layer_2),
                "w3": np.random.randn(output_layer, hidden_layer_2) * np.sqrt(1./output_layer)
            }
        finally:
            self.output_file = weightsFile
            

    # hidden layer activation function: sigmoid - maps all values between 0 and 1
    def sigmoid(self, x, derivative=False):
        if derivative:
            return (np.exp(-x))/((np.exp(-x)+1)**2)
        return 1/(1+np.exp(-x))

    # output activation function: softmax - converts the raw machine probabilities into regular ass probabilities
    def softmax(self, x, derivative=False):
        exps = np.exp(x-x.max())
        if derivative:
            return exps / np.sum(exps, axis=0) * (1-exps / np.sum(exps, axis=0))
        return exps/np.sum(exps, axis=0)


    def forward_pass(self, x_train):
        params = self.params

        params["a0"] = x_train # sets the activation matrix dim[784*1]

        #input to hidden layer 1
        params["z1"] = np.dot(params["w1"], params["a0"]) #dot product of weight and activation [128*784]dot[784*1] = [128*1]
        params["a1"] = self.sigmoid(params["z1"])

        #hidden layer 1 to hidden layer 2
        params["z2"] = np.dot(params["w2"], params["a1"]) #dot product of weight and activation [64*128]dot[128*1] = [64*1]
        params["a2"] = self.sigmoid(params["z2"])

        # hidden layer 2 to output
        params["z3"] = np.dot(params["w3"], params["a2"]) #dot product of weight and activation [10*64]dot[64*1] = [10*1]
        params["a3"] = self.softmax(params["z3"])

        return params["z3"]


    def backward_pass(self, y_train, output):
        params = self.params

        change_w = {}

        #calculate w3 update
        error = 2 * (output - y_train) / output.shape[0] * self.softmax(params["z3"], derivative=True)
        change_w["w3"] = np.outer(error, params["a2"])

        #calculate w2 update
        error = np.dot(params["w3"].T, error) * self.sigmoid(params["z2"], derivative=True)
        change_w["w2"] = np.outer(error, params["a1"])

        #calculate w1 update
        error = np.dot(params["w2"].T, error) * self.sigmoid(params["z1"], derivative=True)
        change_w["w1"] = np.outer(error, params["a0"])

        return change_w


    def update_weights(self, change_w):
        for key, val in change_w.items():
            self.params[key] -= self.lr * val # W_t+1 = W_t - lr * delta_W_t


    def train(self, x_train, y_train, x_test, y_test, epochs, lr):
        self.lr = lr
        # number of iterations of passing all the data and updating weights
        for j in range(epochs):
            start_time = time.time()
            # one complete round of passing all the inputs and updating weights
            for i in range(len(x_train)):
                values = x_train[i].split(",")
                inputs = (np.asarray(values, dtype=float) / 255.0 * 0.99) + 0.01
                targets = np.zeros(10) + 0.01
                targets[int(y_train[i])] = 0.99
                output = self.forward_pass(inputs)
                change_w = self.backward_pass(targets, output)
                self.update_weights(change_w)
            
            accuracy = self.compute_accuracy(x_test, y_test)
            print("Epoch: {0}, Time spent: {1:.02f}s, Accuracy: {2:.2f}%".format(j+1, time.time()-start_time, accuracy*100))
            if (accuracy >= self.accuracy):
                outputFile = open(self.output_file, "w")
                self.accuracy = accuracy
                weights = ["w1", "w2", "w3"]
                for weight in weights:
                    flattened_array = self.params[weight].flatten()
                    outputFile.write(",".join(map(str, flattened_array)) + "\n")
                outputFile.write(str(self.accuracy))
                outputFile.close()


    def compute_accuracy(self, x_test, y_test):
        predictions = []
        for i in range(len(x_test)):
            values = x_test[i].split(",")
            inputs = (np.asarray(values, dtype=float) / 255.0 * 0.99) + 0.01
            targets = np.zeros(10) + 0.01
            targets[int(y_test[i])] = 0.99
            output = self.forward_pass(inputs)
            pred = np.argmax(output)
            predictions.append(pred==np.argmax(targets))

        return np.mean(predictions)


    def predict(self, test_data):
        predictions = []
        values = test_data.split(",")
        inputs = (np.asarray(values[0:], dtype=float) / 255.0 * 0.99) + 0.01
        output = self.forward_pass(inputs)
        pred = np.argmax(output)
        predictions.append(pred)
        print(str(pred))
        return predictions
