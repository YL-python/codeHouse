"""
不同类型的紧急情况的次数
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\simkai.ttf')
fill_path = r"911.csv"
df = pd.read_csv(fill_path)
print(df.info())
# print(df.head(1))

# 问题一
# 写法1  找出所有分类--构造0数组--计数求和
"""
title_list = df['title'].str.split(':').tolist()
cate_list = list(set([i[0] for i in title_list]))
print(cate_list)

# 构造全为0 的数组

# 一维方法
# zero_temp = pd.Series(np.zeros(len(cate_list)), index=cate_list)
# print(zero_temp)
# for cate in cate_list:
#     zero_temp[cate] = sum(df['title'].str.contains(cate))
# print(zero_temp)

# 二维方法
zero_temp = pd.DataFrame(np.zeros((df.shape[0], len(cate_list))),
                         columns=cate_list)
# print(zero_temp)
for cate in cate_list:
    zero_temp[cate][df['title'].str.contains(cate)] = 1
sum_ret = zero_temp.sum(axis=0)
print(sum_ret)
"""

# 写法二  新加一列分类数据 用groupby 来做
title_list = df['title'].str.split(':').tolist()
cate_list = [i[0] for i in title_list]
df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))
# print(df.head(5))
cate_sum = df.groupby(by='cate')['title'].count()

_x = cate_sum.index
_y = cate_sum.values
plt.figure(figsize=(10, 6), dpi=80)
plt.bar(_x, _y)
plt.grid(alpha=0.4)
plt.show()
