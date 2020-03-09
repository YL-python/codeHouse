import numpy as np

ndarray = np.random.randint(0, 100, size=(5, 5))
n_min = ndarray.min()
n_max = ndarray.max()

print((ndarray - n_min) / (n_max - n_min))
