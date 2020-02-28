"""
处理数据
"""
import json
import pandas as pd


data_str = open('herolist.json', encoding='utf-8').read()
if data_str.startswith(u'\ufeff'):
    data_str = data_str.encode('utf-8')[3:].decode('utf-8')
data = json.loads(data_str, encoding='utf-8')

data_list = []
for i in data:
    temp = {}
    temp['cname'] = i['cname']
    temp['hero_type'] = i['hero_type']
    temp['title'] = i['title']
    # temp['skin_name'] = i['skin_name']  # 不说所有数据都有skin_name属性所以会报错
    data_list.append(temp)

t = pd.DataFrame(data_list)
print(t)
