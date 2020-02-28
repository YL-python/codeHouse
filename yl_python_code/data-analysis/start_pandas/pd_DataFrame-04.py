import pandas as pd
import numpy as np

df = pd.read_csv(r'E:\PyCharm2019\data-analysis\start_pandas\dogNames2.csv')
df_sorted = df.sort_values(by='Count_AnimalName', ascending=False)

# 索引 两种方式
# - 方括号写数组,表示取行,对行进行操作
# - 写字符串表示的取列索引，对列进行操作

# print(df_sorted[:20])
# print(df_sorted[:20]['Row_Labels'])
# print(type(df_sorted[:20]['Row_Labels']))  # series 类型

df = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('ABC'), columns=list('WXYZ'))
# print(df)
# - df.loc[]  通过标签索引数据  方括号
# - df.iloc[]  通过位置获取数据  0开始
# - pandas里面 二维是DataFrame类型  一维是series类型  单个数据是numpy类型
print(df.loc[['A', 'C'], ['W', 'Z']])
print(df.loc['B':, ['W', 'Z']])
print(df.loc['A':'C', ['W', 'Z']])

print(df.iloc[[0, 2], [1, 3]])
print(df.iloc[1:, [1, 3]])
print(df.iloc[0:2, [1, 3]])

# 修改数据
df.loc[['A', 'C'], ['W', 'Z']] = 100
print(df)
