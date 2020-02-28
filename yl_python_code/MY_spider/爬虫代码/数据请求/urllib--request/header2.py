# konachan_spider.默认加请求头方式 
import urllib.request
import urllib.parse

url='http://ilovefishc.com/'

head={"User-Agent":"Mozilla/5.0 (Windows NT 6.konachan_spider; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
#定义 User-Agent

request = urllib.request.Request(url,headers=head)#创建请求对象并且传入定义的head

response = urllib.request.urlopen(request)
#用urlopen访问对象并用responsea接受返回的数据

#print(request.headers)#查看请求头信息
#查看请求头第二种方法 直接调用函数 print(对象名. get_header ("User-agent"))
#调用函数时参数只有首字母大写且必须大写
print(response.read().decode())


"""
自己写了head后 不管http还是https 都可以获得百度的内部代码
写了head后相当于告诉浏览器我是用户我是安全的
"""

