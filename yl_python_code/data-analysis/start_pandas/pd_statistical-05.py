"""

"""
import pandas as pd

fill_path = "starbucks_store_worldwide.csv"
df = pd.read_csv(fill_path)
# print(df.head(5))
# print(df.info())

# df 自带的分组函数
group_Country = df.groupby(by='Country')
# print(group_Country)
# 返回值是一个 DataFrameGroupBy 对象  操作：遍历 - 聚合

# # 每一个值都是一个二值元组 一个值是Country 一个值是所有分类的DF数组
# for i,j in group_Country:
#     print(i)
#     print('_'*20)
#     print(j)
#     print('*'*20)
# US_data = df[df['Country']=='US']

# 获取美国和中国的数量  还有min max sum mean median 函数  这些方法都不统计nan
country_count = group_Country['Brand'].count()
# print(country_count['US'])
# print(country_count['CN'])

china_data = df[df['Country'] == "CN"]
group_china = china_data.groupby(by='State/Province')['Brand'].count()
# print(group_china)


# 数据多条件分组
grouped = df["Brand"].groupby(by=[df["Country"], df["State/Province"]]).count()
print(grouped)
# 是series类型 前面两个是索引
# 因为 df["Brand"] 是series类型  所以分组时候的返回值是series类型

# 三种方法返回 DATa Frame 类型   df[["Brand"]]是DataFrame类型
grouped1 = df[["Brand"]].groupby(by=[df["Country"], df["State/Province"]]).count()
grouped2 = df.groupby(by=[df["Country"], df["State/Province"]])[["Brand"]].count()
grouped3 = df.groupby(by=[df["Country"], df["State/Province"]]).count()[["Brand"]]

# 索引操作  行标
print(grouped1.index)
grouped1.index = ['', '']  # 修改索引
grouped1.reindex(['', ''])  # 有返回值 获取索引 有的就赋原值，没有就是nan
grouped1.set_index('a', drop=False)  # 把a这一列的值作为索引  drop表示是否保留a这一列
grouped1.index.unique()  # 返回index的唯一值
grouped1.set_index(['',''])  # 可以设置复合索引
