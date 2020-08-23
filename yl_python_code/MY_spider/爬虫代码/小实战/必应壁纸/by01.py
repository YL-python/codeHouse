'''
https://cn.bing.com/th?id=OHR.{{key}}_{{分辨率}}.jpg
key是下面爬的
分辨率支持
    UHD  4K
    1920x1200
    1920x1080
    1366x768
    1280x768
    1024x768
    800x600
    800x480
    768x1280
    720x1280
    640x480
    480x800
    400x240
    320x240
    240x320
例子：
    https://cn.bing.com/th?id=OHR.TahoeBeach_ZH-CN3786728560_UHD.jpg
    https://cn.bing.com/th?id=OHR.UrquhartCastle_ZH-CN9360986614_1920x1080.jpg
    https://cn.bing.com/th?id=OHR.UrquhartCastle_ZH-CN9360986614_640x480.jpg

'''

import requests
import json
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
url = "https://bing.ioliu.cn/?p={}"

try:
    allData = json.load(open("by.json", "r", encoding='utf-8'))
except:
    allData = []

for i in range(1, 137):
    print("正在爬取第 {} 页".format(i))
    html_doc = requests.get(url.format(i), headers=HEADERS).content.decode('utf-8')
    soup = BeautifulSoup(html_doc, 'lxml')
    titleList = soup.select('.description h3')
    timeList = soup.select('.calendar .t')
    viewList = soup.select('.view .t')
    likeList = soup.select('.options .heart .t')
    downloadList = soup.select('.options .download .t')
    keyList = soup.select('.options .download')

    for index in range(len(titleList)):
        item = {}
        item["title"] = titleList[index].get_text()
        item["time"] = timeList[index].get_text()
        item["view"] = viewList[index].get_text()
        item["like"] = likeList[index].get_text()
        item["download"] = downloadList[index].get_text()
        item["key"] = keyList[index].get('href').replace("/photo/", "").replace("?force=download", "")
        allData.append(item)

json.dump(allData, open("by.json", "w", encoding='utf-8'), ensure_ascii=False)
