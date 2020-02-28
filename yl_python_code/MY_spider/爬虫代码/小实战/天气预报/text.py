'''
去除空格

with open('E:\pycharm\爬虫代码\小实战\天气预报\\123.txt','r',encoding='UTF-8')as f:
    # print(f)
    data = f.readlines()
    # print(data)
    # two = open('E:\pycharm\爬虫代码\小实战\天气预报\\456.txt','a',encoding='UTF-8')
    for i in data:
        if i is '\n':
            pass
        else:
            with open('E:\pycharm\爬虫代码\小实战\天气预报\\456.txt','a',encoding='UTF-8')as m:
                m.write(i)
            # print(i)
'''

'''
import re
import json
num = {}
with open('E:\pycharm\爬虫代码\小实战\天气预报\\city.txt','r',encoding='UTF-8')as f:
    data = f.readlines()
    # print(data)
    for i in data:
        i = re.sub(r"[\s]", '', i)
        a, b = i.split('=')
        num[b]=a

data_1 = json.dumps(num)
with open('city.json','w')as f:
    f.write(data_1)
    
处理字符串并且转成json代码
'''

'''
读json文件

import json
with open('city.json','r')as f:
    result = json.load(f)
    print(result['彭泽'])
    
'''
