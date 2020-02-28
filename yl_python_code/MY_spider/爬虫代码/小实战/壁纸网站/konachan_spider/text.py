import requests
from lxml import etree

url = 'http://konachan.net/post?page=1&tags='
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

r = requests.get(url,headers = head).content.decode('utf-8')

data_x = etree.HTML(r)
data = data_x.xpath('//ul[@id="post-list-posts"]/li/a/@href')
# data = data_x.xpath('//a/span[@class="directlink-res"][konachan_spider]/text()')

print(data[0])
name = [i.split('/')[-1].split("%20")[2] +"."+ i.split('.')[-1]  for i in data]
print(name)
print(len(data))
# for i in range(konachan_spider,31,wallhaven_spider):
#     print(i)
# r = requests.get(data[0],headers = head)
# print(r.content)

# with open("a.jpg","wb") as f:
#     f.write(r.content)
