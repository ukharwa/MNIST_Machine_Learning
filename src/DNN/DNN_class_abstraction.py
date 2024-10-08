import numpy as np

class DNN:
    def __init__(self, size, output_file="std_output.txt"):
        self.accuracy = 0
        
        self.num_layers = len(size)
        self.params = {}

        for i in range(1, len(size)):
            self.params["w" + str(i)] = np.random.randn(size[i], size[i - 1]) * np.sqrt(1./size[i])
            

    def sigmoid(self, x, derivative=False):
        if derivative:
            return (np.exp(-x))/((np.exp(-x)+1)**2)
        return 1/(1+np.exp(-x))

    def softmax(self, x, derivative=False):
        exps = np.exp(x-x.max())
        if derivative:
            return exps / np.sum(exps, axis=0) * (1-exps / np.sum(exps, axis=0))
        return exps/np.sum(exps, axis=0)

    def forward_pass(self, x_train):
        params = self.params
        edges = self.num_layers - 1

        params["a0"] = x_train

        for i in range(1, edges):
            params["z" + str(i)] = np.dot(params["w" + str(i)], params["a" + str(i - 1)])
            params["a" + str(i)] = self.sigmoid(params["z" + str(i)])

        params["z" + str(edges)] = np.dot(params["w" + str(edges)], params["a" + str(edges - 1)])
        params["a" + str(edges)] = self.softmax(params["z" + str(edges)])
        
        return params["z" + str(edges)]

    def back_prop(self):
        pass

    def update_weights(self, change_w):
        for key, val in change_w.items():
            self.params[key] -= self.lr * val # W_t+1 = W_t - lr * delta_W_t

    def train(self, train_data, test_data, epochs, learning_rate):
        pass

    def compute_accuracy(self, test_data):
        pass

    def predict(self, prediction_data):
        pass

