import requests
import json
import os
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
IDURL = 'https://www.rimeito.com/mingzhan/yalayi/page/{}/'
INFOURL = 'https://www.rimeito.com/{}.html/'


def getIdList():
    id_list = []
    for i in range(1, 23):
        url = IDURL.format(i)
        html_doc = requests.get(url).content.decode('utf-8')
        soup = BeautifulSoup(html_doc, 'lxml')
        ids = soup.select('#posts .post .img a')
        for id in ids:
            id_url = id.get('href').replace("https://www.rimeito.com/", '').replace(".html/", '')
            id_list.append(id_url)
    return id_list


def getinfo(id_list):
    info_list = []
    size = len(id_list)
    for index in range(size):
        id = id_list[index]
        print("正在爬取 {} 的信息...进度 {}/{}".format(id, index + 1, size + 1))
        url = INFOURL.format(id)
        html_doc = requests.get(url).content.decode('utf-8')
        soup = BeautifulSoup(html_doc, 'lxml')
        infos = soup.select(".article-content > p")[-1].get_text().split('\n')
        print(infos)
        item = {}
        item['id'] = id
        item['套图名称'] = infos[0].split('：')[1]
        item['图分辨率'] = infos[1].split('：')[1]
        item['套图大小'] = infos[2].split('：')[1]
        item['解压密码'] = infos[4].split('：')[1]
        info_list.append(item)
    return info_list


def main():
    try:
        id_list = json.load(open("ids.json", "r", encoding='utf-8'))
    except:
        id_list = getIdList()
        json.dump(id_list, open("ids.json", "w", encoding='utf-8'), ensure_ascii=False)
    try:
        info_list = json.load(open("infos.json", "r", encoding='utf-8'))
    except:
        info_list = getinfo(id_list)
        json.dump(info_list, open("infos.json", "w", encoding='utf-8'), ensure_ascii=False)


if __name__ == '__main__':
    main()
