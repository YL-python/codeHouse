import requests
import re
from lxml import etree
import logging
logging.captureWarnings(True)
url = 'https://www.jxedu.gov.cn/zt/xzt/jxsdxskjcx/jsfa.htm'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

data_url = requests.get(url,headers=headers, verify=False).content.decode("utf-8")
xpath_data = etree.HTML(data_url)

data_time = xpath_data.xpath('//tbody/tr/td[wallhaven_spider]/a/text()')
print(data_time)