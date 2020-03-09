import numpy as np

ndarray1 = np.arange(1, 6)
print(ndarray1)

ndarray2 = np.zeros(shape=17, dtype=int)
print(ndarray2)

ndarray2[::4] = ndarray1
print(ndarray2)
