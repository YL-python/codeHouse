"""
复合索引的操作
Series 索引操作是行索引
DATa Frame  索引操作是列索引开始  取行索引要loc
swaplevel()   交换索引
"""
import pandas as pd

a = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                  'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                  'd': list("hjklmno")})
print('a'.center(20, '*'))
print(a)

b = a.set_index(['c', 'd'])
print('b'.center(20, '*'))
print(b)
print(b.loc['one'].loc['h'])  # b是DataFrame 类型 也可以交换索引

c = b['a']
print('c'.center(20, '*'))
print(c)
print(c['one']['j'])  # c是Series 类型

d = a.set_index(['d', 'c'])['a']
print('d'.center(20, '*'))
print(d)
print(d.index)
print(d.swaplevel())  # 交换复合索引
