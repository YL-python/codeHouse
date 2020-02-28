import pandas as pd

df = pd.read_csv(r'E:\PyCharm2019\data-analysis\start_pandas\dogNames2.csv')
# print(df.head())
# print(df.info())

# DataFrame 中排序的方法  按什么排序  升序还是降序
df = df.sort_values(by='Count_AnimalName', ascending=False)
print(df)
