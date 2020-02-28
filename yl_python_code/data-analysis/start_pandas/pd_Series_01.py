"""
Series 代标签的一维数组

"""

import pandas as pd

# 创建方法一 可以指定数据和下标
t1 = pd.Series([1, 2, 3, 4], index=list("ABCD"), dtype=float)
# print(t1)
# print(t1.dtype)  # 查看数据类型 修改数据类型 指定数据类型   和numpy一样
# t1.astype('int64')
# print(t1)
# print(type(t1))

# 创建方法二 用字典创建
temp_dict = {'name': "xiaohong", "age": 18, 'tel': 10086}
t2 = pd.Series(temp_dict)
# print(t2)

# 切片和索引
# print(t2['age'])  # 键值取数据
# print('*'*20)
# print(t2[0])  # 索引取数据
# print('*'*20)
# print(t2[0:3])  # 取连续数据
# print('*'*20)
# print(t2[[0,2]])  # 取不连续数据
# print(t2[['age', 'tel']])  # 取不连续数据
# print(t2[['age','h']])  # 强行取不存在的值会nan

# 获取下标和值
# print(t2.index)   # 可迭代
# list(t2.index)  # 可迭代对象都可强制类型转换成列表
# print(t2.values)

# np可以用的方法都可以用在Series上  argmax  clip
print(t1.where(t1 > 1.0))
print(t1.where(t1 > 1.0, 10))
print(t1.mask(t1 > 1.0))

#  tolist()  能把series转换成列表
