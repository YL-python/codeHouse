# 需求分析
# 有标题：世界最登對的姊妹搭檔中出逆3P三明治性愛
# 图片：https://mmslt1.com/nvyou/20190410/sMnktqBu.jpg
# 时间：20190410
# 名称：sMnktqB
# 视频id：71762
# 播放链接：https://www.96fhk.com/shipin/play-71762.html?road=1
# 播放链接：https://www.96fhk.com/shipin/play-71762.html?road=2
# m3u8文件链接：https://s1.maomibf1.com/common/nvyou/20191128/sMnktqBu/sMnktqBu.m3u8
# m3u8文件链接：https://s1.maomibf2.com/common/nvyou/20191128/sMnktqBu/sMnktqBu.m3u8

import requests
from lxml import etree


url = "https://www.96fhk.com/shipin/nvyou-%E6%9C%89%E5%9D%82%E6%B7%B1%E9%9B%AA-1.html"
url_head = "https://www.96fhk.com"
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
x_title = 'x_title = "//div[@id="tpl-img-content"]/li/a/@title"'  # 标题
x_href = '//div[@id="tpl-img-content"]/li/a/@href'  # id
x_img = '//div[@id="tpl-img-content"]/li/a/img/@data-original'  # 图片

data = requests.get(url,headers=header).content.decode()
data_xpath = etree.HTML(data)
data_title = data_xpath.xpath('//div[@id="tpl-img-content"]/li/a/img/@data-original')
print(data_title)