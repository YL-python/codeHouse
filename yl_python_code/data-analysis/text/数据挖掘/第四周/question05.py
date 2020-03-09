import numpy as np

ndarray53 = np.random.randint(0, 100, size=(5, 3))
print(ndarray53)

ndarray32 = np.random.randint(0, 100, size=(3, 2))
print(ndarray32)

print(np.dot(ndarray53, ndarray32))
