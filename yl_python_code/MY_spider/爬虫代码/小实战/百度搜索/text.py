import requests
from lxml import etree
url = 'https://www.baidu.com/s?wd=计算机&pn=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

data_url = requests.get(url,headers=headers).content.decode("utf-8")
xpath_data = etree.HTML(data_url)

data1 = xpath_data.xpath('//div[@id="content_left"]/div[3]//div[@class="c-abstract"]/text()')
data2 = xpath_data.xpath('//div[@id="content_left"]/div[3]//div[@class="c-abstract"]/em/text()')

# data = data.xpath('')
print(data1)
print(data2)
