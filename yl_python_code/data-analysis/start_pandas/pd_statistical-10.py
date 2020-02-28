"""
时间序列
统计出911数据中
不同月份电话次数的变化情况
不同月份不同类型紧急电话的次数的变化情况
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""  date_range  函数简介
# 生成时间序列 start开始日期  end结束日期  periods生成个数  freq间隔单位 D M 10D
data1 = pd.date_range(start='20181231', end='20190131', freq='D')
# print(data1)
data2 = pd.date_range(start='20181231', periods=10, freq='M')
# print(data2)

# 把时间序列做成行索引
index = pd.date_range('20170101', periods=10)
df1 = pd.DataFrame(np.random.rand(10), index=index)
# print(df1)
"""

fill_path = r"911.csv"
df = pd.read_csv(fill_path)

# 加一列分类数据
title_list = df['title'].str.split(':').tolist()
cate_list = [i[0] for i in title_list]
df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))

# to_datetime 标准化时间序列 要是时间序列不标准就传format 参数
# 时间字符串设置为标准时间类型并且设置为时间索引
df['timeStamp'] = pd.to_datetime(df['timeStamp'], format='')
df.set_index('timeStamp', inplace=True)

# 重采样函数 计数修改时间索引的时间单位  resample('M').mean()/count()/max... 时间索引的操作
count_by_month = df.resample('M').count()['title']

_x = count_by_month.index
_y = count_by_month.values
_x = [i.strftime('%Y-%m-%d') for i in _x]
plt.figure(figsize=(15, 10), dpi=80)
plt.plot(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x, rotation=45)
plt.grid(alpha=0.4)
plt.show()

plt.figure(2, figsize=(15, 10), dpi=80)
for group_name, group_data in df.groupby('cate'):
    count_by_month = group_data.resample('M').count()['title']
    _x = count_by_month.index
    _y = count_by_month.values
    _x = [i.strftime('%Y-%m-%d') for i in _x]
    plt.plot(range(len(_x)), _y, label=group_name)
plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc="best")
plt.grid(alpha=0.4)
plt.show()
