import numpy as np

ndarray = np.ones(shape=(8, 8), dtype=int)
ndarray[::2, ::2] = 0
ndarray[1::2, 1::2] = 0
print(ndarray)
