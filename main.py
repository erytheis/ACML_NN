import numpy as np
import random


def sig(x):
    res = 1 / (1 + np.exp(-x))
    return res


def calculate_errors(X, A):
    D = np.sum([X, -A], axis = 0)
    return D


def dsig(x):
    dsig = (sig(x)) * (1 - sig(x))
    return dsig


def reinitialize_derivatives():
    DeltaW2 = np.zeros((numOfHiddenNodes, numOfInputNodes))
    DeltaW3 = np.zeros((numOfOutputNodes, numOfHiddenNodes))
    Deltab2 = np.zeros((numOfHiddenNodes, 1))
    Deltab3 = np.zeros((numOfOutputNodes, 1))
    return {"DW2": DeltaW2,
            "Db2": Deltab2,
            "DW3": DeltaW3,
            "Db3": Deltab3}

# def forward_prop(numOfInputNodes, numOfHiddenNodes, numOfOutputNodes):




# initial parameters
numOfInputNodes = 8
m = 8
numOfHiddenNodes = 3
numOfLayers = 3
numOfOutputNodes = 8

ALPHA = 0.9
LAMBDA = 0.0001

samples = np.identity(8)
# FORWARD PROPAGATION
# layer 0
A1 = np.array([0, 1, 0, 0, 0, 0, 0, 0])
A1 = A1.reshape(8, 1)

# layer 1
W2 = np.random.rand(numOfHiddenNodes, A1.shape[0]) * 0.01
b2 = np.random.rand(numOfHiddenNodes, 1) * 0.01
Z2 = np.dot(W2, A1) + b2
A2 = sig(Z2)
##### CHECK HERE FOR SHAPES     assert(Z.shape == (W.shape[0], A.shape[1]))

# layer 2
W3 = np.random.rand(numOfOutputNodes, A2.shape[0]) * 0.01
b3 = np.random.rand(numOfOutputNodes, 1) * 0.01
Z3 = np.dot(W3, A2) + b3
A3 = sig(Z3)

# save the error dynamics
err_dynamics = []

for i in range(20000):

    # GRADIENT DESCENT
    # initializing dz
    deltas = reinitialize_derivatives()

    for sample in samples:

        A1 = sample.reshape(8, 1)

        # FORWARD PROPAGATION
        # layer 2
        Z2 = np.dot(W2, A1) + b2
        A2 = sig(Z2)

        # layer 3
        Z3 = np.dot(W3, A2) + b3
        A3 = sig(Z3)

        # BACKPROPAGATION
        # compute the cost
        D3 = -np.sum([A1, -A3], axis = 0)

        D2 = np.multiply(np.dot(W3.T, D3), dsig(Z2))

        err_dynamics.append(D3)

        # compute derivative
        dW3 = np.dot(D3, A2.T)
        db3 = D3
        dW2 = np.dot(D2, A1.T)
        db2 = D2

        # update DeltaW
        deltas["DW3"] += dW3
        deltas["DW2"] += dW2
        deltas["Db3"] += db3
        deltas["Db2"] += db2

    # update descent parameters
    W3 = W3 - ALPHA * (1 / m * deltas["DW3"] + LAMBDA * W3)
    W2 = W2 - ALPHA * (1 / m * deltas["DW2"] + LAMBDA * W2)
    b3 = b3 - ALPHA * (1 / m * deltas["Db3"])
    b2 = b2 - ALPHA * (1 / m * deltas["Db2"])


def test(INPUT):
    A1 = INPUT.reshape(8, 1)

    # FORWARDPROPAGATION
    # layer 2
    Z2 = np.dot(W2, A1) + b2
    A2 = sig(Z2)

    # layer 3
    Z3 = np.dot(W3, A2) + b3
    A3 = sig(Z3)

    return A3


print((test(samples[3])))
