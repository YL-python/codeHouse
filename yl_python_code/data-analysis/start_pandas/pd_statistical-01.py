"""
电影数据中评分的平均分，导演的人数等信息分的平均分，导演的人数等信息
"""
import pandas as pd

fill_path = r'E:\PyCharm2019\data-analysis\start_pandas\IMDB-Movie-Data.csv'
df = pd.read_csv(fill_path)
print(df.info())
# print(df.head(1))

# 获取平均得分
rating_mean = df['Rating'].mean()

# 获取导演人数  可能一个导演拍了很多片子
# director_num = len(set(df['Director'].tolist()))
# unique() 出现一次
director_num = len(df['Director'].unique())

# 获取演员人数
temp_actors_list = df['Actors'].str.split(',').tolist()
actors_list = [i for j in temp_actors_list for i in j]
actors_num = len(actors_list)

# 获取最大值，最小值，中值
max_Runtime = df['Runtime (Minutes)'].max()
max_Runtime_index = df['Runtime (Minutes)'].argmax()
min_Runtime = df['Runtime (Minutes)'].min()
min_Runtime_index = df['Runtime (Minutes)'].argmin()
median_Runtime = df['Runtime (Minutes)'].median()
