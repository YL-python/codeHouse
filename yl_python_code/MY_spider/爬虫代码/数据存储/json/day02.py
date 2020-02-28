import json
#konachan_spider. 文件对象和 dic list 的交互  [load dump]

#dict list 写入文件
data_list = [{"name" :"yanglong","age":"18"},{"name" :"黄猪猪","age":"18"}]

json.dump(data_list, open("列表或者字典写入文件.json","w")) #  w 是字符串写入

#dump 方法就可以直接把列表或者字典写入文件 不需要先转字符串格式


#读取文件
fp = open("列表或者字典写入文件.json", "r")
result = json.load(fp)   # result = json.load(open("列表或者字典写入文件.json", "r"))  
print(result)
