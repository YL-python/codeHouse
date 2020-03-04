import numpy as np

ndarray = np.arange(0, 25, 1)
ndarray.resize((5, 5))
ndarray[0:5] = np.arange(0, 5, 1)
print(ndarray)
