import numpy as np


class Net:
    def __init__(self, wlayers, nlayers, use_bias=True):
        for index, w in enumerate(wlayers):
            wlayers[index] = np.array(w)

        self.wlayers = wlayers
        self.use_bias = use_bias
        self.nlayers = nlayers

    def act(self, x):
        return 0 if x < 0.5 else 1

    @staticmethod
    def perceptron(x):
        return 0 if x < 0.5 else 1

    def go(self, y):
        y = np.array(y)
        for layer_index, w in enumerate(self.wlayers):
            act = self.nlayers[layer_index]
            if self.use_bias:
                y = np.concatenate([y, np.array([1])])

            y = np.dot(w, y)
            y = np.array([act[i](x) for i, x in enumerate(y)])

        return y[0]
