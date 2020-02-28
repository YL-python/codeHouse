import pandas as pd
# import numpy as np

df = pd.read_csv(r'E:\PyCharm2019\data-analysis\start_pandas\dogNames2.csv')
df_sorted = df.sort_values(by='Count_AnimalName', ascending=False)

# - 布尔索引  &并且  |或者   字符串函数都可以用
print(df[(800 < df['Count_AnimalName']) & (df['Count_AnimalName'] < 1000)])
print(df[(df['Row_Labels'].str.len() > 4) & (df['Count_AnimalName'] > 700)])
