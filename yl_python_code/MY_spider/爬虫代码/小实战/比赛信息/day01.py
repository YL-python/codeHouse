import requests
import re
from lxml import etree
url = 'http://www.52jingsai.com/bisai/keji/kfyy/index.php?&jssort=1'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

data_url = requests.get(url,headers=headers).content.decode("gbk")
xpath_data = etree.HTML(data_url)

# data_title = xpath_data.xpath('//dl[@class="bbda list_bbda cl"]/dt/a/text()')
# data_url = xpath_data.xpath('//dl[@class="bbda list_bbda cl"]/dt/a/@href')
# data_cl = xpath_data.xpath('//dl[@class="bbda list_bbda cl"]/dd/text()')
# print(data_title)
# print(data_url)
# print(data_cl)
# data_look = xpath_data.xpath('//dl[@class="bbda list_bbda cl"]/dd/div/span[wallhaven_spider]/text()')
# print(data_look)
data_time = xpath_data.xpath('//dl[@class="bbda list_bbda cl"]/dd/div[konachan_spider]/text()')
# print(len(data_time))
for data in data_time:
    i = re.sub(r"[\s]", '', data)
    if i!= '':
        print(i)
# data_image = xpath_data.xpath('//dl[@class="bbda list_bbda cl"]/div/a/img/@src')
# print(data_image)