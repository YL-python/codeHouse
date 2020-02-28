import requests
from lxml import etree

ZHUTI = "dongman"
FILEPATH = "F:\\图片\\bian_img\\{}\\".format(ZHUTI)
URL_HEAD = "http://www.netbian.com"

url = 'http://www.netbian.com/{}/index_XXX.htm'.format(ZHUTI)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}


url = url.replace("XXX", "2")
r = requests.get(url,headers=headers).content.decode("gbk")

data_x = etree.HTML(r)
data = data_x.xpath('//div[@class="list"]/ul/li/a/@href')

data_url1 = [URL_HEAD+i for i in data ]

# print(data)
# print(len(data))
#
# print(data_url1)

r = requests.get(data_url1[0],headers=headers).content.decode("gbk")

data_x = etree.HTML(r)
data = data_x.xpath('//div[@class="pic-down"]/a/@href')

url2 = URL_HEAD+data[0]
r = requests.get(url2,headers=headers).content.decode("gbk")
# print(r)
data_x = etree.HTML(r)
data = data_x.xpath('//td[@align="left"]/a/@href')
print(data)
