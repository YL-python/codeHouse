'''
https://www.ecy1.com/category/cymt


'''

import requests
import json
from lxml import etree

url = 'https://www.ecy1.com/wp-admin/admin-ajax.php?action=zrz_load_more_posts'
url2='https://www.ecy1.com/16418.html'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
data = {'type': 'catL13',
        'paged': '1'}
# response = requests.post(url, headers=head,data=data).text
# response = json.loads(response)
# print(len(response))
# print(response["msg"])
# data_x = etree.HTML(response["msg"])
# data = data_x.xpath('//h2[@class="entry-title"]/a/@href')
# print(data)

data = requests.get(url2, headers=head).text
data_x = etree.HTML(data)
data2 = data_x.xpath('//figure[@class="content-img-box "]/img/@src')
print(data2)