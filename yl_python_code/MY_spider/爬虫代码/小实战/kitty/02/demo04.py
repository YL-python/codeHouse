import requests
import json
import re
import time
import functools
from bs4 import BeautifulSoup

url = "https://www.4cc1cb1f9661.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

try:
    allData = json.load(open("index3.json", "r", encoding='utf-8'))
except:
    allData = []
print("当前数量：{}".format(len(allData)))
def del_null(str):
    return re.sub(r"[\s/]", '', str)



for people in range(len(allData)):
    print("正在爬取第 {} 个人".format(people))
    html_doc = requests.get(url + allData[people]['id'], headers=HEADERS).content.decode('utf-8')
    soup = BeautifulSoup(html_doc, 'lxml')
    allData[people]['list'] = []
    # 抓取当前页
    infoList = soup.select('#tpl-img-content li a')
    dataList = soup.select('#tpl-img-content .down_date')
    for index in range(len(infoList)):
        item = {}
        item['id'] = infoList[index].get('href')
        item['title'] = infoList[index].get('title')
        item['date'] = del_null(dataList[index].get_text())
        allData[people]['list'].append(item)
    # 获取页码
    allpage = len(soup.select('.pagination .hidden-xs'))
    if allpage > 1:
        for page in range(2, allpage + 1):
            print("正在爬取第 {} 个人 第{} 页".format(people, page))
            html_doc_son = requests.get(url + allData[people]['id'].replace(".html", "-{}.html".format(page)),
                                        headers=HEADERS).content.decode('utf-8')
            soup_son = BeautifulSoup(html_doc_son, 'lxml')
            infoList_son = soup_son.select('#tpl-img-content li a')
            dataList_son = soup_son.select('#tpl-img-content .down_date')
            for index in range(len(infoList_son)):
                item_son = {}
                item_son['id'] = infoList_son[index].get('href')
                item_son['title'] = infoList_son[index].get('title')
                item_son['date'] = del_null(dataList_son[index].get_text())
                allData[people]['list'].append(item_son)

print("当前数量：{}".format(len(allData)))
json.dump(allData, open("index4.json", "w", encoding='utf-8'), ensure_ascii=False)
