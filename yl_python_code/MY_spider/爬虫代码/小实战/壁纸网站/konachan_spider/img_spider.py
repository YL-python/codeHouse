"""
查看图片详细用  https://konachan.net/post/show/ + 图片名称的数字
"""
import requests
from lxml import etree
import os

IMG_SEAVE_PATH = 'E:\\图片\\konachan_img\\'
MAIN_URL = 'http://konachan.net/post?page={}&tags='
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}


def exist_file(name):
    if os.path.exists(IMG_SEAVE_PATH+name):
        return True
    else:
        return False


def my_requests(url):
    response1 = requests.get(url, headers=HEADERS)
    if response1.status_code != 404:
        return response1.content
    else:
        response2 = requests.get(url.replace("jpg", "png"), headers=HEADERS)
        if response2.status_code != 404:
            return response2.content
        else:
            print('有问题：' + url)
            return None


def main():
    IMG_NUM = 0
    for i in range(1,10000):
        print("正在爬取第{}页".format(i).center(50,"-"))
        try:
            result = my_requests(MAIN_URL.format(i)).decode("utf-8")
            data_x = etree.HTML(result)
            data_img = data_x.xpath('//ul[@id="post-list-posts"]/li/a/@href')
        except:
            print("出现异常本次爬取结束，一共爬取{}张图片".format(IMG_NUM))
        for temp in range(len(data_img)):
            IMG_NUM += 1
            img_name = data_img.split('/')[-1].split("%20")[2] + "." + data_img.split('.')[-1]
            if(exist_file(img_name)):
                print('\r第{}页第{}张图片已存在'.format(i,temp+1),end='')
            else:
                img_data = my_requests(data_img[temp])
                if (img_data != None):
                    print('\r正在下载第{}页,第{}张图片'.format(i, temp + 1), end='')
                    with open(IMG_SEAVE_PATH + img_name, "wb")as f:
                        f.write(img_data)
        print()
        print("第{}页获取完毕,总获取{}张图片".format(i,IMG_NUM))


main()