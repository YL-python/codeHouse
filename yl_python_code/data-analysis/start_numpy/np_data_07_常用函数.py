"""
2019年8月24日18点45分
numpy 的常用函数

"""
import numpy as np
t1 = np.arange(24).reshape((4, 6))
# 求和函数  sum
print(t1.sum(axis=0))
print(np.sum(t1, axis=0))

# 求均值   mean
print(t1.mean(axis=0))

# 求中值   median
print(np.median(t1, axis=0))

# 最大最小值   max min
print(t1.max(axis=0))
print(t1.min(axis=0))
# print(np.min(t1,axis=0))

# 极值(max-min)   ptp
print(np.ptp(t1, axis=0))

# 标准差 = sqrt(方差)   std
print(t1.std(axis=0))
# print(np.std(t1,axis=0))

# 获取最大值最小值在数组中的位置
print(np.argmax(t1, axis=0))
print(np.argmin(t1, axis=0))

# 创建全0，全1，对角线为1的方阵
print(np.zeros((3, 4)))
print(np.ones((3, 4)))
print(np.eye(3))
