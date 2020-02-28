"""

"""
import pandas as pd
import matplotlib.pyplot as plt

file_path = r'PM2.5/BeijingPM20100101_20151231.csv'
df = pd.read_csv(file_path)
# print(df.info())
# print(df.head(1))

# 把分开的时间字符串通过 PeriodIndex方法转换为 pandas的时间类型
period_data = pd.PeriodIndex(year=df['year'], month=df['month'],
                             day=df['day'], hour=df['hour'], freq='H')
# print(period_data)
# print(type(period_data))
df['date_time'] = period_data

# 设置时间索引
df.set_index('date_time', inplace=True)

# 降采样
df = df.resample('7D').mean()

# 处理缺失值 1 删除
data = df['PM_US Post'].dropna()
data_china = df['PM_Dongsi'].dropna()
# print(data_china.tail(10))  # 后n行数据

_x = data.index
_y = data.values
_x_china = data_china.index
_y_china = data_china.values
plt.figure(figsize=(15, 10), dpi=80)
plt.plot(range(len(_x)), _y, label='PM_US Post')
plt.plot(range(len(_x_china)), _y_china, label='PM_Dongsi')
plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)
plt.grid(alpha=0.4)
plt.legend()
plt.show()

