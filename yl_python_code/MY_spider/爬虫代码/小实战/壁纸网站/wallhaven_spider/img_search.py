import requests
import json
import os
from bs4 import BeautifulSoup
from hyper.contrib import HTTP20Adapter

categories = "111"  # 种类# 种类 按顺序三个参数是 General（一般）/ Anime（动漫）/ People（人物） 1表示选择，0表示不选择
purity = "111"  # 图片纯度  按顺序是 sfw(安全的) / sketchy(粗略的) / nsfw(不安全的)  1表示选择，0表示不选择
sortingList = ["favorites", "date_added", "views"]  # 规则
sorting = sortingList[0]  # 选择排序方式

IMG_SEAVE_PATH = 'E:\\图片\\wallhaven\\search\\'  # 保存路径
URL = 'https://wallhaven.cc/search?categories={}&purity={}&sorting={}&order=desc'.format(categories, purity, sorting)
IMG_URL = "https://w.wallhaven.cc/full/{}/wallhaven-{}.{}"
id_filter = []
IMG_SEAVE_PATH_CONTENT = []

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

# 过滤函数
def fun_filter(obj):
    if obj['id'] in id_filter:
        return False
    else:
        id_filter.append(obj['id'])
        return True


# 判断文件是否存在
def exist_file(name):
    if name in IMG_SEAVE_PATH_CONTENT:
        return True
    else:
        return False


# 获取所有信息
def get_all_img_info(search_txt):
    try:
        all_search_data = json.load(open(os.path.join(IMG_SEAVE_PATH, search_txt + ".json"), "r", encoding='utf-8'))
    except:
        all_search_data = []
    max_page = -1
    old_len = len(all_search_data)
    for page in range(1, 20):
        # 退出
        if max_page != -1 and page > max_page:
            break
        print("正在爬取第 {} 页，进度 {}/{}".format(page, page, max_page))
        url = URL + '&page={}&q={}'.format(page, search_txt)
        HEADERS[':path'] = '/' + url.split('/')[-1]
        sessions = requests.session()
        sessions.mount(url, HTTP20Adapter())
        html_doc = sessions.get(url, headers=HEADERS, timeout=5).content.decode("utf-8", "ignore")
        soup = BeautifulSoup(html_doc, 'lxml')
        # 获取最大页数
        if max_page == -1:
            all_num = int(soup.select('.listing-header h1')[0].get_text().split(" ")[0].replace(",", ''))
            max_page = all_num // 24 + 1

        img_info_list = soup.select('.thumb-listing-page ul li figure')
        for img_info in img_info_list:
            # print(img_info)
            item = {}
            item['id'] = img_info['data-wallpaper-id']
            purity_list = img_info['class']
            if 'thumb-nsfw' in purity_list:
                item['purity'] = 'nsfw'
            elif "thumb-sketchy" in purity_list:
                item['purity'] = 'sketchy'
            else:
                item['purity'] = 'sfw'
            item['size'] = img_info.select('.thumb-info .wall-res')[0].get_text()
            if len(img_info.select('.thumb-info .png')) == 0:
                item['cate'] = 'jpg'
            else:
                item['cate'] = 'png'
            all_search_data.append(item)
    all_search_data = list(filter(fun_filter, all_search_data))
    new_len = len(all_search_data)
    print("文件开始时数量为：{}，爬取完成后数量为{}。".format(old_len, new_len))
    json.dump(all_search_data, open(os.path.join(IMG_SEAVE_PATH, search_txt + ".json"), "w", encoding='utf-8'),
              ensure_ascii=False)


# 读取文件保存图片
def read_jsan_to_save(search_txt):
    try:
        data_list = json.load(open(os.path.join(IMG_SEAVE_PATH, search_txt + ".json"), "r", encoding='utf-8'))
    except:
        data_list = []
    data_len = len(data_list)
    for index in range(data_len):
        item = data_list[index]
        filename = '{}_{}_{}.{}'.format(item['purity'], item['id'], item['size'].replace(" ", ''), item['cate'])
        print("正在爬取：{}，进度 {}/{}".format(filename, index, data_len))
        if not exist_file(filename):
            url = IMG_URL.format(item['id'][0:2], item['id'], item['cate'])
            try:
                response = requests.get(url, headers=HEADERS2, timeout=5)
                if response is not None:
                    file_name = os.path.join(IMG_SEAVE_PATH, filename)
                    with open(file_name, "wb")as f:
                        f.write(response.content)
            except Exception as e:
                print("爬取失败：{}，错误原因是:{}。".format(url, e))


def main(search_txt):
    # 先爬取全部信息保存到本地
    get_all_img_info(search_txt)
    # 读取文件遍历保存图片
    read_jsan_to_save(search_txt)


if __name__ == '__main__':
    # search_txt = 'rem'
    # search_txt = 'Kaguya-Sama'
    # search_txt = 'Chika Fujiwara'
    # search_txt = 'Miku'
    # search_txt = 'Eromanga-sensei'
    search_txt = 'genshin%20impact'
    try:
        IMG_SEAVE_PATH = os.path.join(IMG_SEAVE_PATH, search_txt)
        os.makedirs(IMG_SEAVE_PATH)
    except Exception as e:
        pass
    IMG_SEAVE_PATH_CONTENT = os.listdir(IMG_SEAVE_PATH)
    main(search_txt)
