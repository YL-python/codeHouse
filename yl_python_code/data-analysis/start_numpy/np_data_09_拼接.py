'''
拼接 va/hstack 需要传入元组参数
行列交换

'''

import numpy as np

t1 = np.arange(12).reshape(2, 6)
t2 = np.arange(12, 24).reshape(2, 6)
print(t1)
print(t2)

# 竖直方向拼接
print(np.vstack((t1, t2)))
# 水平方向拼接
print(np.hstack((t1, t2)))

t1[:, [0, 1]] = t1[:, [1, 0]]
print(t1)
t2[[0, 1], :] = t2[[1, 0], :]
print(t2)
