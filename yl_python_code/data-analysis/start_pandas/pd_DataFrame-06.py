import pandas as pd
import numpy as np

t = pd.DataFrame(np.arange(24).reshape(4, 6), index=list('ABCD'), columns=list('UVWXYZ'))
t.loc[['A', 'C'], ['V', 'X']] = np.nan

# 看数值是不是nan
print(pd.isnull(t))
print(pd.notnull(t))

# dropna 删除nan所在的行列
# how参数 all表示全部是nan才删除 any表示有一个是nan就删除
# inplace False表示有返回值（不对原数据修改）  True 表示无返回值（在原数据上修改）
print(t.dropna(axis=0, how='any', inplace=False))

# fillna 填充是nan的数据  有返回值
# pandas 计算均值时会忽略nan
print(t.fillna(t.mean()))
t['X'] = t['X'].fillna(t['X'].mean())  # 只填充某一列
print(t)

# 处理是0的数据  有的时候0是有误数据
t[t == 0] = np.nan
