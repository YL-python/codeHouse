import requests
import json
import re
import time
import functools
from bs4 import BeautifulSoup

url = "https://www.4cc1cb1f9661.com/shipin/list-%E5%A5%B3%E4%BC%98%E4%B8%93%E8%BE%91-{}.html"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

try:
    allData = json.load(open("index3.json", "r", encoding='utf-8'))
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

def del_null(str):
    return re.sub(r"[\s/]", '', str)


for page in range(1, 6):
    print("正在爬取第 {} 页".format(page))
    html_doc = requests.get(url.format(page), headers=HEADERS).content.decode('utf-8')
    soup = BeautifulSoup(html_doc, 'lxml')
    nameList = soup.select('#tpl-img-content li a')
    for index in range(len(nameList)):
        item = {}
        item['id'] = nameList[index].get('href')
        item['name'] = nameList[index].get('title')
        allData.append(item)


allData = list(filter(fun_filter, allData))
print("当前数量：{}".format(len(allData)))
json.dump(allData, open("index3.json", "w", encoding='utf-8'), ensure_ascii=False)
