# �������
# �б��⣺������ǌ�����ô�n�г���3P�������Ԑ�
# ͼƬ��https://mmslt1.com/nvyou/20190410/sMnktqBu.jpg
# ʱ�䣺20190410
# ���ƣ�sMnktqB
# ��Ƶid��71762
# �������ӣ�https://www.96fhk.com/shipin/play-71762.html?road=1
# �������ӣ�https://www.96fhk.com/shipin/play-71762.html?road=2
# m3u8�ļ����ӣ�https://s1.maomibf1.com/common/nvyou/20191128/sMnktqBu/sMnktqBu.m3u8
# m3u8�ļ����ӣ�https://s1.maomibf2.com/common/nvyou/20191128/sMnktqBu/sMnktqBu.m3u8

import requests
from lxml import etree


url = "https://www.96fhk.com/shipin/nvyou-%E6%9C%89%E5%9D%82%E6%B7%B1%E9%9B%AA-1.html"
url_head = "https://www.96fhk.com"
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
x_title = 'x_title = "//div[@id="tpl-img-content"]/li/a/@title"'  # ����
x_href = '//div[@id="tpl-img-content"]/li/a/@href'  # id
x_img = '//div[@id="tpl-img-content"]/li/a/img/@data-original'  # ͼƬ

data = requests.get(url,headers=header).content.decode()
data_xpath = etree.HTML(data)
data_title = data_xpath.xpath('//div[@id="tpl-img-content"]/li/a/img/@data-original')
print(data_title)