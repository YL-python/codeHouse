import pandas as pd
import json


# pandas都csv文件
# dog_names = pd.read_csv('./dogNames2.csv')
# print(dog_names)


# pandas读取json文件
data_str = open('herolist.json', encoding='utf-8').read()
# 去除BOM隐藏字符
if data_str.startswith(u'\ufeff'):
    data_str = data_str.encode('utf-8')[3:].decode('utf-8')
# json文件转python格式
data_list = json.loads(data_str, encoding='utf-8')
# print(type(data_list))
t = pd.DataFrame(data_list)
print(t)
