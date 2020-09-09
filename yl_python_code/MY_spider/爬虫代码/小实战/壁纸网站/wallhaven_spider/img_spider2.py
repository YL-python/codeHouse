import requests
import time
import json
import os
from lxml import etree


# 种类 按顺序三个参数是 General（一般）/ Anime（动漫）/ People（人物） 1表示选择，0表示不选择
categories = "010"  # 种类
# 图片纯度  按顺序是 sfw(安全的) / sketchy(粗略的) / nsfw(不安全的)  1表示选择，0表示不选择
purity="110"
topRangeList = ["1M", "3M", "6M", "1y", "1w", "1d", "3d"]  # 时间
sortingList = ["toplist", "favorites", "toplist-beta", "views"]  # 规则
MAX_PAGE = 10  # 爬取最大页数
DAY = time.strftime("%Y-%m-%d", time.localtime())  # 今天日期
IMG_SEAVE_PATH = 'E:\\图片\\wallhaven\\'  # 保存路径
URL = 'https://wallhaven.cc/search?categories={}&purity={}&topRange={}&sorting={}&order=desc&page=@'
IMG_URL = "https://w.wallhaven.cc/full/{}/wallhaven-{}"
XPATH_STR = '//section[@class="thumb-listing-page"]/ul/li/figure/@data-wallpaper-id'
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

topRangeDict = {"1M":"01-一个月内","3M":"02-三个月内","6M":"03-六个月内","1y":"04-一年内","1w":"05-一周内","1d":"06-一天内","3d":"07-三天内"}
sortingDict = {"toplist": "01-排行榜", "favorites":"02-喜欢数", "toplist-beta":"03-最佳测试版", "views":"04-观看数"}

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
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code != 404:
            return etree.HTML(response.content.decode("utf-8","ignore")).xpath(XPATH_STR)
        else:
            return None
    except Exception as e:
        print("爬取失败：" + url)
        print("错误原因是：", e)
        return None


def request_img(dir, name):
    url = IMG_URL.format(name[0:2], name)
    try:
        response = requests.get(url + ".jpg", headers=HEADERS, timeout=3)
        if response.status_code == 404:
            response = requests.get(url + ".png", headers=HEADERS, timeout=3)
        if response is not None:
            file_name = os.path.join(dir, response.url.split("-")[-1])
            with open(file_name,"wb")as f:
                f.write(response.content)
    except Exception as e:
        print("爬取失败：" + url)
        print("错误原因是：", e)

def write_msg(data):
    with open(os.path.join(IMG_SEAVE_PATH,DAY,"message.txt"),"w")as f:
        f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'),ensure_ascii=False))


def get_msg():
    file_path = os.path.join(IMG_SEAVE_PATH,DAY)
    sortingList = os.listdir(file_path)
    all_msg = []
    for sorting in sortingList:
        msg = {}
        msg[sorting[3:]] = {}
        sorting_path = os.path.join(file_path,sorting)
        if os.path.isdir(sorting_path):
            topRangeList = os.listdir(sorting_path)
            s_t_size = 0
            for topRange in topRangeList:

                s_t_path = os.path.join(sorting_path,topRange)
                if os.path.isdir(s_t_path):
                    files = os.listdir(s_t_path)
                    size = sum([os.path.getsize(os.path.join(s_t_path,file)) for file in files])
                    s_t_size += size
                    msg[sorting[3:]][topRange[3:]] = "图片数量：" + str(len(files))
            msg[sorting[3:]]["文件夹大小"] = "{:.2f}M".format(s_t_size/1024/1024)
        all_msg.append(msg)
    write_msg(all_msg)


def main():
    for sorting in sortingList:
        for topRange in topRangeList:
            try:
                dir = os.path.join(IMG_SEAVE_PATH, DAY, sortingDict[sorting], topRangeDict[topRange])
                os.makedirs(dir)
            except Exception as e:
                print(e)
            url = URL.format(categories, purity, topRange, sorting)
            for page in range(1, MAX_PAGE+1):
                url_page = url.replace("@", str(page))
                print("正在爬取：" + url_page)
                nameList = request_page(url_page)
                if nameList is not None:
                    for name in nameList:
                        if not exist_file(IMG_SEAVE_PATH, name):
                            print("正在爬取" + name)
                            request_img(dir, name)
    get_msg()


if __name__ == '__main__':
    main()
