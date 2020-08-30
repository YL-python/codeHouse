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
    allData = json.load(open("index5.json", "r", encoding='utf-8'))
except:
    allData = []
print("当前数量：{}".format(len(allData)))

for people in range(len(allData)):
    for list_index in range(len(allData[people]['list'])):
        print("正在爬取第 {} 个人  进度：{}/{}".format(people, list_index, len(allData[people]['list'])))
        if "download" in allData[people]['list'][list_index].keys():
            continue
        else:
            html_doc = requests.get(url.format(allData[people]['list'][list_index]['id']),
                                    headers=HEADERS).content.decode(
                'utf-8')
            soup = BeautifulSoup(html_doc, 'lxml')
            allData[people]['list'][list_index]['download'] = soup.select('#lin1k1')[0].get('value')
        if list_index % 10 == 0:
            json.dump(allData, open("index5.json", "w", encoding='utf-8'), ensure_ascii=False)
    json.dump(allData, open("index5.json", "w", encoding='utf-8'), ensure_ascii=False)

print("当前数量：{}".format(len(allData)))
json.dump(allData, open("index5.json", "w", encoding='utf-8'), ensure_ascii=False)
