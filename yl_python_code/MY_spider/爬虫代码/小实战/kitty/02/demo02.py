import requests
import json
import re
import time
import functools
from bs4 import BeautifulSoup

url = "https://www.4cc1cb1f9661.com{}"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

try:
    allData = json.load(open("index.json", "r", encoding='utf-8'))
except:
    allData = []
print("当前数量：{}".format(len(allData)))

for index in range(len(allData)):
    print("正在爬取第 {} 条数据".format(index))

    if "download" in allData[index].keys():
        continue
    else:
        html_doc = requests.get(url.format(allData[index]['id']), headers=HEADERS).content.decode('utf-8')
        soup = BeautifulSoup(html_doc, 'lxml')
        allData[index]['download'] = soup.select('#lin1k1')[0].get('value')
    if index % 10 == 0:
        json.dump(allData, open("中文字幕.json", "w", encoding='utf-8'), ensure_ascii=False)

print("当前数量：{}".format(len(allData)))
json.dump(allData, open("中文字幕.json", "w", encoding='utf-8'), ensure_ascii=False)
