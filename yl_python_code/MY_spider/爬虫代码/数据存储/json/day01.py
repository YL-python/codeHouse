import json

#konachan_spider. 字符串和 dic list的交互（转换）[loads  dumps]

# 字符串(要求是标准的json字符串)转——dict list
data_str = '[{"name" :"yanglong","age":"18"},{"name" :"黄猪猪","age":"18"}]'
data_list = json.loads(data_str)

print(data_str)
print(type(data_str))
print(data_list)
print(type(data_list))

# dict list转—— json字符串
data2_list = [{"name" :"yanglong","age":"18"},{"name" :"黄猪猪","age":"18"}]
data2_str = json.dumps(data2_list)
print(data2_str)
print(type(data2_str))



#标准json字符串写法
'''
data_str = '[{"name" :"yanglong","age":"18"},{"name" :"黄猪猪","age":"18"}]'
data_str = {"name" :"yanglong","age":"18"}
'''
