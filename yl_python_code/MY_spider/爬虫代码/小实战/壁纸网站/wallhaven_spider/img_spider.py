"""
查看图片详细用  https://wallhaven.cc/w/ + 图片名称的数字
"""
import requests
from lxml import etree
import os

topRangeList = ["1d", "3d", "1M", "6M","3M", "1y", "1w"]
sortingList = ["toplist", "favorites", "views"]
IMG_SEAVE_PATH = 'E:\\图片\\day\\'
# IMG_SEAVE_PATH = 'E:\\wallhaven_img\\SFW\\'
MAIN_URL = 'https://wallhaven.cc/search?categories=010&purity=100&topRange=abcd&sorting=efgh&order=desc&page={}'
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
MAX_PAGE = 10


def exist_file(name):
    if os.path.exists(IMG_SEAVE_PATH+name):
        return True
    else:
        return False


def my_requests(url):
    try:
        response1 = requests.get(url, headers=HEADERS,timeout=3)
        if response1.status_code != 404:
            return response1.content
        else:
            response2 = requests.get(url.replace("jpg","png"), headers=HEADERS,timeout=3)
            if response2.status_code!=404:
                return response2.content
            else:
                return None
    except:
        return None


def main():
    IMG_NUM = 0
    for sorting in sortingList:
        for topRange in topRangeList:
            url = MAIN_URL.replace('abcd',topRange).replace('efgh',sorting)
            for page_num in range(1,MAX_PAGE+1):
                print("正在爬取第{}页".format(page_num).center(50,"-"))
                try:
                    result = my_requests(url.format(page_num)).decode("utf-8")
                    data_x = etree.HTML(result)
                    img_id = data_x.xpath('//section[@class="thumb-listing-page"]/ul/li/figure/@data-wallpaper-id')
                    for temp in range(len(img_id)):
                        img_name = img_id[temp] + ".jpg"
                        img_url = "https://w.wallhaven.cc/full/{}/wallhaven-{}".format(
                            img_name[0:2], img_name)
                        if (exist_file(img_name)):
                            print('\r第{}页,第{}张图片已存在'.format(page_num, temp + 1), end='')
                        else:
                            img_data = my_requests(img_url)
                            if (img_data != None):
                                print('\r正在下载第{}页,第{}张图片'.format(page_num, temp + 1), end='')
                                with open(IMG_SEAVE_PATH + img_name, "wb")as f:
                                    f.write(img_data)
                                IMG_NUM += 1
                            else:
                                print("\n"+img_url+"获取失败")
                    print("\n第{}页获取完毕,本次获取{}张图片,一共有{}张图片".format(page_num, IMG_NUM, len(os.listdir(IMG_SEAVE_PATH))))
                except:
                    print(url.format(page_num))
                    print("主页面出现异常本次爬取结束，一共爬取{}张图片".format(IMG_NUM))
            print(topRange+"以内排序规则为"+sorting+"的前{}页壁纸爬取完毕".format(MAX_PAGE))
    print("爬完啦")

main()