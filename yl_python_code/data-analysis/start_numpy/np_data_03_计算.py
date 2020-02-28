"""
2019年8月23日10点26分
数组的计算
nan = 0/0 = not a number
inf = 无穷
数组的计算符合 广播原则
"""

import numpy as np
a = np.arange(24)
a = a.reshape((4, 6))
# 数组和数计算
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/0)  # 报警告

# 数组和数组计算  同维度计算
b = np.arange(100, 124).reshape((4, 6))
print(a+b)

# 数组和数组计算  不同维度计算  但是要有一个维度相同  在相同维度上多次计算
c = np.arange(0, 6).reshape((1, 6))
print(a+c)

d = np.arange(0, 4).reshape((4, 1))
print(a+d)
