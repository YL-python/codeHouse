import json
import time

data_time = int(time.time()*1000)
path = "lib/JsonData"
url = 'http://www.nmc.cn'
time_url = 'http://www.nmc.cn/f/rest/real/{}?_={}'


def get(province,city):
    print("正在解析  {} {}  对应的文件，并获取网页链接！".format(province,city))
    ans = list()
    result_city = json.load(open("{}/cityProvince.json".format(path), "r"))
    for temp in result_city:
        if temp['name'] == province:
            city_code = temp['code']
            break
    result = json.load(open("{}/{}.json".format(path, city_code), "r"))
    for temp in result:
        if temp['city'] == city:
            url1 = url + temp['url']
            ans.append(url1)
            url2 = time_url.format(temp['code'], data_time)
            ans.append(url2)
            break
    return ans


def province_list():
    ans = list()
    result_city = json.load(open("{}/cityProvince.json".format(path), "r"))
    for temp in result_city:
        ans.append(temp['name'])
    return ans


def city_list(province):
    ans = ['请选择市区']
    result_city = json.load(open("{}/cityProvince.json".format(path), "r"))
    for temp in result_city:
        if temp['name'] == province:
            city_code = temp['code']
            break
    result = json.load(open("{}/{}.json".format(path, city_code), "r"))
    for temp in result:
        ans.append(temp['city'])
    return ans

if __name__ == '__main__':
    get("江西省","抚州")
    # province_list()
    # city_list("江西省")