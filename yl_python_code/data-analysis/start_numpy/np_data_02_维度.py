'''
2019年8月23日09点03分

查看数组的大小形状维度   shape  [行，列]
reshape  改变维度
reshape：有返回值，所谓有返回值，即不对原始多维数组进行修改；
resize：无返回值，所谓有返回值，即会对原始多维数组进行修改；

flatten()  把数据转成一维
'''


import numpy as np

a = np.arange(12)
print('a'.center(20, "*"))
print(a)
print(a.shape)     # shape可以查看数组的形状

b = np.array([[1, 2, 3], [1, 2, 3]])
print('b'.center(20, "*"))
print(b)
print(b.shape)

c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,5,6]]])
print('c'.center(20,"*"))
print(c)
print(c.shape)

d = np.arange(12)
print('d'.center(20,"*"))
print(d)
print(d.reshape((3,4)))         #  reshape可以修改数组的形状

e = np.arange(24)
print('e'.center(20,"*"))
print(e)
print(e.reshape((2,3,4)))    # [块，行，列]

print(e.reshape( (24,) ))   # 一维
print(e.reshape( (1,24) ))  # 二维 一行24列
print(e.reshape( (24,1) ))  # 二维 24行一列

# 计算一个数据的个数
e = e.reshape((4,6))          # 三维数组还要*shape[2]
num = e.shape[0]*e.shape[1]   # 一维数组会报错没有shape[1]
print(num)

# 上面方法还是要知道数据的维度才好操作
e = e.reshape((2,3,4))   # 测试 不管几维数据flatten都可以吧数据一维展开
print(e.flatten() )   # flatten() 把数据一维展开  有返回值

