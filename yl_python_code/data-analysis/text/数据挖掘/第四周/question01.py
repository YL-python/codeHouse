import numpy as np

ndarray = np.random.randint(0, 100, size=(2, 3, 3, 3))
print(ndarray)

ndarray_sum = ndarray.sum(axis=(2, 3))

print(ndarray_sum)
