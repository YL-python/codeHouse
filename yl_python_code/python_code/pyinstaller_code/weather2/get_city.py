import requests
import json
import os

url = 'http://www.nmc.cn/f/rest/province'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                         '537.36 (KHTML, like Gecko) Chrome/'
                         '74.0.3729.131 Safari/537.36'}
response = requests.get(url, headers=headers).content.decode("utf-8")
data_list = json.loads(response)  # 把标准字符串变成 list

try:
    os.mkdir(".\\jsonFile")
except:
    pass

json.dump(data_list, open("jsonFile/cityProvince.json", "w"))

result = json.load(open("jsonFile/cityProvince.json", "r"))
print(result)
for temp in result:
    city_name ="/" + temp['url'].split('/')[3].split('.')[0]
    file_name = "jsonFile" + city_name + ".json"
    response = requests.get(url+city_name, headers=headers).content.decode("utf-8")
    data_list = json.loads(response)
    json.dump(data_list, open("{}".format(file_name), "w"))
    print(response)