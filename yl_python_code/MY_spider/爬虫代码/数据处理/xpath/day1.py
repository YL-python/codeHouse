from lxml import etree  #导入模块 xpath只是这个模块里面的一个语法
import requests

url = 'http://www.netbian.com/'
head ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}

#打开指定网页转译成字符串
data_str = requests.get(url,headers = head).content.decode('gbk')

#转解析类型 变成XPath可以解析的类型
data_xpath = etree.HTML(data_str)   #调用函数

#调用xpath方法
#data = data_xpath.xpath('//li/a/text()')    获取所有li 标签下 所有a标签里面内容 
#data = data_xpath.xpath('//li/a[@href="/desk/21824.htm" ]/b/text()')#获取li标签下 一个指定属性的a标签 下b标签的了内容
#data = data_xpath.xpath('//li/a/@href')     #获取所有li标签下面所有a 标签里面href属性的内容
#data = data_xpath.xpath('//li/a[@href="/desk/21827.htm"]/b/text()')

data = data_xpath.xpath('//a[@href="/desk/21827.htm"]/img/@src')    #找 特定a标签里面img标签里面src属性的值

print(data[0])

'''
konachan_spider. 先导包  from lxml import etree
wallhaven_spider. 转xpath可以解析的数据类型   .etree.HTML('neiron')
3. 调用方法  wenben.xpath(' /  // [@]  @  text() ')
模糊查询  //div[contains[@class,'a']]   所有的div有class='a' 属性 的我们都要
下一个节点（平级关系）  /following-sibling::*     取当前节点的下一节点
'''
 
