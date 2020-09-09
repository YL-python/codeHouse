import requests
import time
import json
import os
from lxml import etree
from hyper.contrib import HTTP20Adapter


# 种类 按顺序三个参数是 General（一般）/ Anime（动漫）/ People（人物） 1表示选择，0表示不选择
categories = "001"  # 种类
# 图片纯度  按顺序是 sfw(安全的) / sketchy(粗略的) / nsfw(不安全的)  1表示选择，0表示不选择
purity="001"
topRangeList = ["1M", "3M", "6M", "1y", "1w", "1d", "3d"]  # 时间
sortingList = ["toplist", "favorites", "toplist-beta", "views"]  # 规则
MAX_PAGE = 15  # 爬取最大页数
DAY = time.strftime("%Y-%m-%d", time.localtime())+"fuli"  # 今天日期
IMG_SEAVE_PATH = 'E:\\图片\\wallhaven\\'  # 保存路径
URL = 'https://wallhaven.cc/search?categories={}&purity={}&topRange={}&sorting={}&order=desc&page=@'
IMG_URL = "https://w.wallhaven.cc/full/{}/wallhaven-{}"
XPATH_STR = '//section[@class="thumb-listing-page"]/ul/li/figure/@data-wallpaper-id'
HEADERS = {':authority': 'wallhaven.cc',
           ':method': 'GET',
           ':path': '',
           ':scheme': 'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9',
           'cookie': '__cfduid=de79da98f23853031b031fe462a175fff1571829951; _pk_ref.1.01b8=%5B%22%22%2C%22%22%2C1577340676%2C%22https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%3A%2F%2Fwallhaven.cc%2F%22%5D; _pk_testcookie.1.01b8=1; _pk_ses.1.01b8=1; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlJZRSt6bVFnUUhMNU1HdExPVUNpWVE9PSIsInZhbHVlIjoibFhrZ2c1YUNFaGdcLzZpc0xvSFBBcGRTZStqZmwxXC9CRmZOUTRZN0Q1cm1PV2pQekZ4MHFaUElJbTM5WHltUnJQZm5tWE9lYnRqc2I0UDhPTDNSOVYxUjJzWHFtY0dJSXhSNkoxZTYzU3orbkxWR0IxU3F3dW9XUGFqNGRhNHdNTE4wb2VZQ0lBZVkzcHhzdUhrNGJpR2RLRGNCZmhqZEhPMWQ5WDRtMXFaV1o5K3A2OXFyTG5aZzNLS1hXcGxJdmoiLCJtYWMiOiI4M2JhYTgzOTZjOGFhNjhiODU2YmI4ZDMyMWU1YWMwNDgyNTk0ZDM0NmU5NzYyZjRlNmYzYjEzMTNmMTNiM2Y1In0%3D; XSRF-TOKEN=eyJpdiI6InRQWkxwWmpxSEs5aktGa0dMNnNURmc9PSIsInZhbHVlIjoiMmlWV3pRNjR6TXlDQmliS29mdW9KRnk0K2pTelwvVDlUWnhISkhoS0U1cEJjRHVrNmhwenJONGZBNE5RR25zcjYiLCJtYWMiOiI1MjQ0YTUzZTI0YTM3ZWE5N2IwZjMyYmM5NjNmOTQzNGUzMzUzYzU4NTE1NjgzYzk2M2ViNmNhODMxZDI2MzdjIn0%3D; wallhaven_session=eyJpdiI6IkF0dUduVDlodzExc0hRNzZSNUVGbGc9PSIsInZhbHVlIjoiT1NBYnhMYTBudFQyWFlOK2l0UG5pV3hOdVlhVGVQMjFjZHprWUc5c0JKWlVlWmZ2Z0VyXC9Zbk9sYjRQMlVVOW0iLCJtYWMiOiJiMmE1NTE4MDRjNjIwZTAxNGM1ZjczYzQ3YWFkZDRmY2FkOGE4OTgyZTEwMGI5MzkzYTQ0NDlkYTBmMWMzZjA0In0%3D; _pk_id.1.01b8=214a9398ccc729dc.1571829954.42.1577341889.1577340676.',
           'referer': 'https://wallhaven.cc',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'same-origin',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

HEADERS2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}


def exist_file(path, name):
    name1, name2 = name + ".jpg", name + ".png"
    flag = False
    for root, dirs, files in os.walk(path):
        if files is None:
            continue
        else:
            if name1 in files or name2 in files:
                flag = True
                break

    if flag:
        print(name+"存在了")
    return flag


def request_page(url):
    print("正在爬取：" + url)
    try:
        sessions = requests.session()
        sessions.mount(url, HTTP20Adapter())
        response = sessions.get(url, headers=HEADERS, timeout=5)
        # response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code != 404:
            list = etree.HTML(response.content.decode("utf-8", "ignore")).xpath(XPATH_STR)
            # print(list)
            return list
        else:
            return None
    except Exception as e:
        print("爬取失败：" + url)
        print("错误原因是：", e)
        return None


def request_img(dir, name):
    print("正在爬取" + name)
    url = IMG_URL.format(name[0:2], name)
    try:
        response = requests.get(url + ".jpg", headers=HEADERS2, timeout=5)
        if response.status_code == 404:
            response = requests.get(url + ".png", headers=HEADERS2, timeout=5)
        if response is not None:
            file_name = os.path.join(dir, response.url.split("-")[-1])
            with open(file_name,"wb")as f:
                f.write(response.content)
    except Exception as e:
        print("爬取失败：" + url)
        print("错误原因是：", e)


def main():
    for sorting in sortingList:
        for topRange in topRangeList:
            try:
                dir = os.path.join(IMG_SEAVE_PATH, DAY)
                os.makedirs(dir)
            except Exception as e:
                print(e)
            url = URL.format(categories, purity, topRange, sorting)
            for page in range(1, MAX_PAGE+1):
                url_page = url.replace("@", str(page))
                HEADERS[':path'] = '/' + url_page.split('/')[-1]
                nameList = request_page(url_page)
                if nameList is not None:
                    for name in nameList:
                        if not exist_file(IMG_SEAVE_PATH, name):
                            request_img(dir, name)


if __name__ == '__main__':
    main()
