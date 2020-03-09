import numpy as np

ndarray = np.random.randint(0, 10, (3, 3))
print(ndarray)
ndarray_mean = ndarray.mean(axis=1).reshape(3, 1)
print(ndarray_mean)
print(ndarray-ndarray_mean)
