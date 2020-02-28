import json

# 字符串(要求是标准的json字符串)转——dict list
data_str = '[{"name" :"yanglong","age":"18"},{"name" :"黄猪猪","age":"18"}]'
data_list = json.loads(data_str)

# dict list转—— json字符串
data2_list = [{"name" :"yanglong","age":"18"},{"name" :"黄猪猪","age":"18"}]
data2_str = json.dumps(data2_list)

#dict list 写入文件
data_list = [{"name" :"yanglong","age":"18"},{"name" :"黄猪猪","age":"18"}]
json.dump(data_list, open("列表或者字典写入文件.json","w")) #  w 是字符串写入
#dump 方法就可以直接把列表或者字典写入文件 不需要先转字符串格式

#读取json文件
fp = open("列表或者字典写入文件.json", "r")
result = json.load(fp)   # result = json.load(open("列表或者字典写入文件.json", "r"))
print(result)

#json文件有BOM隐藏字符的处理方法
if data_json.startswith(u'\ufeff'):
    data_json = data_json.encode('utf-8')[3:].decode('utf-8')