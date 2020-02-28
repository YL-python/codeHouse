"""
DataFrame 的一些属性

"""
import json
import pandas as pd


data_str = open('herolist.json', encoding='utf-8').read()
if data_str.startswith(u'\ufeff'):
    data_str = data_str.encode('utf-8')[3:].decode('utf-8')
data_list = json.loads(data_str, encoding='utf-8')
t = pd.DataFrame(data_list)

print(t.index)   # 行索引
print(t.columns)  # 列索引
# print(t.values)  # np.array 数据类型的数据
print(t.shape)
print(t.dtypes)
print(t.ndim)  # 数据维度
# print(t.head())  # 显示数据前n行 默认5
# print(t.tail())  # 显示后几行  默认5
print(t.info())  # 显示数据概览
print(t.describe())  # 对数值类型数据快速统计
