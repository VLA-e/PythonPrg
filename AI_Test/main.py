import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
inputs = np.array([1,1,0]) # 3 input - 3 neurons
weights = np.array([10,2,-5]) # 3 weights - 3 sinopsa [10,0,-5]
outputs = sigmoid(np.dot(inputs, weights)) # rabota vixodnogo neirona
print(outputs)
print(np.dot(inputs, weights))
print(type(inputs))
print(weights.dtype)