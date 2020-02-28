from lxml import etree
import requests
url = 'http://www.netbian.com/desk/21828.htm'

data_url=requests.get(url).content.decode('gbk')

xpath_data = etree.HTML(data_url)

result = xpath_data.xpath('//p/a/img/@src')
print(result)

'''
有时候并不是你的表达式有问题
是数据用ajax技术后期加上去的
所以一开始用xpath  获取不到数据
最佳的办法是先看网页完代码中有没有数据 没有的话就说明是ajax 技术后期加上去的
'''