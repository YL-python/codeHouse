import numpy as np

ndarray = np.random.random(10)
print(ndarray)
ndarray[ndarray.argmax()] = 0
print(ndarray)
