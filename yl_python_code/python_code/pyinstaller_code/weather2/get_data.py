import json
import time

data_time = int(time.time()*1000)

city = ["江西省", "南昌"]
path = "lib/JsonData"
url = 'http://www.nmc.cn'
time_url = 'http://www.nmc.cn/f/rest/real/{}?_={}'
result_city = json.load(open("{}/cityProvince.json".format(path), "r"))


for temp in result_city:
    if temp['name'] == city[0]:
        city_code = temp['code']
        print(temp['code'])
        break

result = json.load(open("{}/{}.json".format(path,city_code), "r"))
print(result[0])
for temp in result:
    if temp['city'] == city[1]:
        url1 = url+temp['url']
        print(url1)
        url2 = time_url.format(temp['code'],data_time)
        print(url2)
        break
