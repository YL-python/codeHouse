import numpy as np

ndarray = np.ones((10, 10))
ndarray[1:-1, 1:-1] = 0
print(ndarray)
