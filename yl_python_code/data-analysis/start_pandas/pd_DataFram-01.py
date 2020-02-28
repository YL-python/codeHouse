"""
DataFrame
index  行索引  axis=0  0轴
columns  列索引  axis=1  1轴
"""

import pandas as pd
import numpy as np

t = pd.DataFrame(np.arange(12).reshape(3, 4))
# print('*'*20)
# print(t)

t0 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('wxyz'))
# print('*'*20)
# print(t0)

d1 = {'name': ['xiaoxiao', 'xiaohong'], 'age': [30, 32], 'tel': [10086, 10010]}
t1 = pd.DataFrame(d1, index=['pep{}'.format(i) for i in range(1, 3)])
# print('*'*20)
# print(t1)

d2 = [{'name': 'xiaoxiao', 'age': 12, 'tel': 11111},
      {'name': 'xiaohong', 'age': 13},
      {'name': 'xiaogangg', 'tel': 22222}]
t2 = pd.DataFrame(d2, index=['pep{}'.format(i) for i in range(1, 4)])
print('*'*20)
print(t2)
