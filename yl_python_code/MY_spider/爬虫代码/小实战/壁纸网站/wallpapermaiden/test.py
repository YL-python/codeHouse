'''
https://www.wallpapermaiden.com/popular?page=1

'''

import requests
import json
from lxml import etree

url = 'https://www.wallpapermaiden.com/popular?page=1'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

response = requests.get(url, headers=head).text
print(len(response))
print(response)
data_x = etree.HTML(response)
data = data_x.xpath('//div[@class="wallpaperBg"]/a/@title')
print(len(data))
print(data)


# url = 'https://www.wallpapermaiden.com/wallpaper/7558/firewatch-forest-landscape-in-game-minimalistic'
# head = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
#
# response = requests.get(url, headers=head).text
# print(len(response))
# print(response)
# data_x = etree.HTML(response)
# data = data_x.xpath('//div[@class="wpBig"]/a/@href')
# print(len(data))
# print(data)

# url = 'https://www.wallpapermaiden.com/wallpaper/7558/firewatch-forest-landscape-in-game-minimalistic/download/3840x2160'
# head = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
#
# response = requests.get(url, headers=head).text
# print(len(response))
# print(response)
# data_x = etree.HTML(response)
# data_1 = data_x.xpath('//div[@class="wpBig wpBigFull"]/a/@href')
# data_2 = data_x.xpath('//div[@class="wpBig wpBigFull"]/a/@title')
# print(len(data_2))
# print(data_2)