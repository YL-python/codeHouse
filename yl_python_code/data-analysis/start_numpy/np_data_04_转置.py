'''
2019年8月24日09点25分
数组的转置
T （大T属性） = transpose()   转置
swapaxes(0,1) 交换轴  轴默认是0，1（二维）  1，0 就是转置了

'''
import numpy as np

t1 = np.arange(24).reshape((4, 6))
print(t1)
print(t1.T)
print(t1.transpose())
print(t1.swapaxes(1, 0))
