import numpy as np

ndarray = np.random.randint(0, 20, size=(5, 5))
print(ndarray)

sort_3_col = np.argsort(ndarray[:, 3])
print(sort_3_col)

print(ndarray[sort_3_col])
