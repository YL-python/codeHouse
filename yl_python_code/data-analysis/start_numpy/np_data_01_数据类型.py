'''
2019年8月22日19点30分

创建np数组  以及查看/修改数据类型

ndarray  numpy的数据格式
np.array(range(10)) = np.arange(10)
dtpye   可以查看也可以指定数据类型   i1 = int8
astype  可以修改数据类型
np.round(x,n)  对x取n位小数
'''
import numpy as np
import random
a = np.array([1,2,3])   # 定义np类型的数据
print('a'.center(20,'*'))
print(a)
print(type(a))          # 返回np的数据数据类型
print(a.dtype)          # 返回a的数据类型  数据类型占内存不一样  存储最大的数值也不一样

print('b'.center(20,'*'))
b = np.array([0,1,0,1],dtype='bool')   # 用dtype='i1'  指定 创建时数据的数据类型
print(b)
print(type(b))
print(b.dtype)   # 返回b的数据类型

print('c'.center(20,'*'))
c = np.arange(12)
print(c)
print(type(c))
print(c.dtype)

print('d'.center(20,'*'))
d = b.astype('int64')       # astype  可以修改数据类型
print(d)
print(d.dtype)

print('e'.center(20,'*'))
e = np.array([random.random() for i in range(10)])
print(e)
f = np.round(e,2)
print(f)