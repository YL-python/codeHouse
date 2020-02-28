import requests
from lxml import etree
import os


ZHUTI = "dongman"
MAX_PAGE = 10
FILEPATH = "F:\\图片\\bian_img\\{}\\".format(ZHUTI)
URL_HEAD = "http://www.netbian.com"


url = 'http://www.netbian.com/{}/index_XXX.htm'.format(ZHUTI)
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/"
                         "537.36 (KHTML, like Gecko) Chrome/"
                         "74.0.3724.8 Safari/537.36"}


def my_requests(imgurl):
    try:
        data = requests.get(imgurl, headers=headers, timeout=3)
        if data.status_code == 404:
            return None
        else:
            return data.content
    except:
        return None


def exist_file(name):
    if os.path.exists(FILEPATH+name):
        return True
    else:
        return False


def seave_img(url, name):
    if exist_file(name):
        print("\r"+name+"已存在",end="")
    else:
        print("\r正在获取" + name, end="")
        img_data = my_requests(url)
        with open(FILEPATH + name, "wb")as f:
            f.write(img_data)



def main():
    IMG_NUM = 0
    for temp1 in range(1,MAX_PAGE):
        print("正在爬取第{}页".format(temp1).center(30,"*"))
        if temp1 == 1:
            url1 = url.replace("_XXX", "")
        else:
            url1 = url.replace("XXX", "{}".format(temp1))
        data = my_requests(url1).decode("gbk")
        if data != None:
            data_x = etree.HTML(data)
            imglist1 = data_x.xpath('//div[@class="list"]/ul/li/a/@href')
            imglist1 = [URL_HEAD + i for i in imglist1]
            for temp2 in imglist1:
                try:
                    data = my_requests(temp2).decode("gbk")
                    data_x = etree.HTML(data)
                    imglist2 = data_x.xpath('//div[@class="pic-down"]/a/@href')
                    url2 = URL_HEAD+imglist2[0]
                    data = my_requests(url2).decode("gbk")
                    data_x = etree.HTML(data)
                    endimgurl = data_x.xpath('//td[@align="left"]/a/@href')[0]
                    filename = endimgurl.split("/")[-1]
                    seave_img(endimgurl,filename)
                    IMG_NUM +=1
                except:
                    pass
        else:
            print(url1+"本次爬取出现异常")
        print("\n第{}页获取完毕,本次获取{}张图片,一共有{}张图片".format(temp1, IMG_NUM, len(os.listdir(FILEPATH))))
    print("完事了")


if __name__ == '__main__':
    main()