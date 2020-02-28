import requests
import time
import re

wenku_url = 'https://wenku.baidu.com/view/123b551252d380eb62946d54.html?sxts=1567129791917'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"}
v_url = 'http://wenku.baiduvvv.com/doc/'
# konachan_spider 在原网页上获取sign 和 t 的值

# data = requests.get(url=url, headers=headers).content
# with open('text.docx','wb')as f:
#     f.write(data)
