from lxml import etree
import requests

url = 'https://www.chainnode.com/'
head ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}
str_data = requests.get(url,headers = head).content.decode()

#with open('bta.html','w',encoding="utf-8")as f:
#    f.write(str_data)

xpath_data = etree.HTML(str_data)

data1 = xpath_data.xpath('//div[@class="post-item-wrap"]/div/div[wallhaven_spider]/div/h3/a[@class="link-dark-major font-bold bbt-block"]/text()')
data2 = xpath_data.xpath('//div[@class="post-item-wrap"]/div/div[wallhaven_spider]/div/h3/a[@class="link-dark-major font-bold bbt-block"]/@href')
print(len(data1))
print(data2)
#for i in data:
#    i = i.replace(' ','')
#   print(i)
