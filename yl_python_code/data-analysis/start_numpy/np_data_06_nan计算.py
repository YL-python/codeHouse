"""
2019年8月24日15点05分
nan (not a number)   读取本地文件发现缺省或者做了一个不合适的计算
inf  无穷大  数除以0的时候
np.count_nonzero()  统计nan 的个数

"""
import numpy as np
a = np.nan
b = np.inf
print(type(a))
print(type(b))

# 两个nan不相等
print(np.nan == np.nan)
print(np.nan != np.nan)

c = np.arange(24,dtype='float').reshape(4,6)
c[:,0] = 0
c[:,2] = np.nan
print(c)
print(c!=c)
print(np.count_nonzero(c))   # 函数统计非0个数
print(np.count_nonzero(c!=c)) # c!=c  只有nan是非0  所以可以用来统计nan  的个数
print(np.isnan(c))   # nan 的地方是True

# nan 进行任何操作结果都是nan
print(np.sum(c,axis=0))   # axis 表示轴的意思 0 是x轴（每一列进行计算）  1是y轴（每一行进行计算）
