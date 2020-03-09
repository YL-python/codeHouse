import numpy as np

ndarray = np.array([1, 2, 3])

A = ndarray.reshape(-1, 1)

B = 2 ** np.arange(3)

M = A & B
M[M != 0] = 1
M[:, ::-1]
print(M)
