import numpy as np
import time

class DNN:
    def __init__(self, size, output_file="std_output.txt"):
        self.accuracy = 0
        self.output_file = output_file
        self.num_layers = len(size)
        self.params = {}

        for i in range(1, len(size)):
            self.params["w" + str(i)] = np.random.randn(size[i], size[i - 1]) * np.sqrt(1./size[i])
            self.params["b" + str(i)] = np.zeros(size[i])
            

    def sigmoid(self, x, derivative=False):
        x = np.clip(x, -500, 500)

        if derivative:
            sig = 1 / (1 + np.exp(-x))
            return sig * (1 - sig)
    
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        exps = np.exp(x-x.max())
        return exps/np.sum(exps, axis=0)

    def forward_pass(self, x_train):
        params = self.params
        edges = self.num_layers - 1

        params["a0"] = x_train

        for i in range(1, edges):
            params["z" + str(i)] = np.dot(params["w" + str(i)], params["a" + str(i - 1)]) + params["b" + str(i)]
            params["a" + str(i)] = self.sigmoid(params["z" + str(i)])

        params["z" + str(edges)] = np.dot(params["w" + str(edges)], params["a" + str(edges - 1)]) + params["b" + str(edges)]
        params["a" + str(edges)] = self.softmax(params["z" + str(edges)])
        
        return params["z" + str(edges)]

    def back_prop(self, y_train, output):
        params = self.params
        edges = self.num_layers - 1
        change_w = {}
        change_b = {}

        loss = output - y_train
        change_w["w" + str(edges)] = np.outer(loss, params["a" + str(edges - 1)])
        change_b["b" + str(edges)] = loss

        for i in range(edges, 1, -1):

            loss = np.dot(params["w" + str(i)].T, loss) * self.sigmoid(params["z" + str(i - 1)], derivative=True)
            change_w["w" + str(i - 1)] = np.outer(loss, params["a" + str(i - 2)])
            change_b["b" + str(i - 1)] = loss

        return change_w, change_b

    def update_params(self, change_w, change_b):
        for key, val in change_w.items():
            self.params[key] -= self.lr * val # W_new = W_old - lr * delta_W
        
        for key, val in change_b.items():
            self.params[key] -= self.lr * val # B_new = B_old - lr * delta_B

    def train(self, x_train, y_train, x_test, y_test, epochs, lr):
        self.lr = lr

        for j in range(epochs):
            start_time = time.time()
            for i in range(len(x_train)):
                values = x_train[i].split(",")
                inputs = (np.asarray(values, dtype=float) / 255.0 * 0.99) + 0.01
                targets = np.zeros(10) + 0.01
                targets[int(y_train[i])] = 0.99
                output = self.forward_pass(inputs)
                change_w, change_b = self.back_prop(targets, output)
                self.update_params(change_w, change_b)
            
            accuracy = self.compute_accuracy(x_test, y_test)
            print("Epoch: {0}, Time spent: {1:.02f}s, Accuracy: {2:.2f}%".format(j+1, time.time()-start_time, accuracy*100))
            
            if accuracy >= self.accuracy:
                self.accuracy = accuracy
                outputFile = open(self.output_file, "w")
                for i in range(1, self.num_layers):
                    flattened_array = self.params["w" + str(i)].flatten()
                    outputFile.write(",".join(map(str, flattened_array)) + "\n")
        
                for i in range(1, self.num_layers):
                    outputFile.write(",".join(map(str, self.params["b" + str(i)])) + "\n")
                
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

    def predict(self, prediction_data):
        values = prediction_data.split(",")
        inputs = (np.asarray(values, dtype=float) / 255.0 * 0.99) + 0.01
        output = self.forward_pass(inputs)
        pred = np.argmax(output)
        predictions.append(pred)
        print(str(pred))

