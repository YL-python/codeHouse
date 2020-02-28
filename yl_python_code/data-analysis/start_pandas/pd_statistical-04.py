"""
数据合并 join merge函数
join 会把行索引相同的合并到一起
merge 按照指定的列把数据按照一定的方式合并到一起
"""
import pandas as pd

data_1 = {'user-name': ['xiaoxiao', 'xiaomin', 'xiaohong', 'xiaogang'],
          'user-age': [18, 19, 20, 21]}
t1 = pd.DataFrame(data_1, index=['pep1', 'pep2', 'pep3', 'pep4'])
print(t1)
data_2 = {'user-name': ['xiaoxiao', 'xiaomin', 'xiaohong', 'xiaolaji'],
          'user-tel': [111, 222, 333, 555]}
t2 = pd.DataFrame(data_2, index=['pep1', 'pep2', 'pep3', 'pep5'])
print(t2)
# print(t2.join(t1))  # 行数和前面的相同

print('inner'.center(20, '*'))
print(pd.merge(t1, t2, on='user-name', how='inner'))  # inner 默认 交集
print('outer'.center(20, '*'))
print(pd.merge(t1, t2, on='user-name', how='outer'))  # outer 并集
print('left'.center(20, '*'))
print(pd.merge(t1, t2, on='user-name', how='left'))  # 左边为准
print('right'.center(20, '*'))
print(pd.merge(t1, t2, on='user-name', how='right'))  # 右边为准
