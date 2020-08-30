import requests
import json
import re
import time
import functools
from bs4 import BeautifulSoup

# url = "https://www.4cc1cb1f9661.com/xiazai/list-%E4%BA%9A%E6%B4%B2%E7%94%B5%E5%BD%B1-{}.html"
url = 'https://www.15edc708571e.com/shipin/list-%E4%B8%AD%E6%96%87%E5%AD%97%E5%B9%95-{}.html'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

try:
    allData = json.load(open("index.json", "r", encoding='utf-8'))
except:
    allData = []
print("当前数量：{}".format(len(allData)))
data_filter = []


def fun_filter(obj):
    if obj['id'] in data_filter:
        return False
    else:
        data_filter.append(obj['id'])
        return True

def cmp(obj_a, obj_b):
    time_a = time.mktime(time.strptime(obj_a['date'], "%Y-%m-%d"))
    time_b = time.mktime(time.strptime(obj_b['date'], "%Y-%m-%d"))
    return time_b - time_a

def del_null(str):
    return re.sub(r"[\s/]", '', str)


for page in range(1, 85):
    print("正在爬取第 {} 页".format(page))
    html_doc = requests.get(url.format(page), headers=HEADERS).content.decode('utf-8')
    soup = BeautifulSoup(html_doc, 'lxml')

    infoList = soup.select('#tpl-img-content .tupian-pic')
    dataList = soup.select('#tpl-img-content .down_date')
    for index in range(len(infoList)):
        item = {}
        item['id'] = infoList[index].get('href')
        item['title'] = infoList[index].get('title')
        item['date'] = del_null(dataList[index].get_text())
        allData.append(item)


allData = list(filter(fun_filter, allData))
allData.sort(key=functools.cmp_to_key(cmp))
print("当前数量：{}".format(len(allData)))
json.dump(allData, open("index.json", "w", encoding='utf-8'), ensure_ascii=False)
