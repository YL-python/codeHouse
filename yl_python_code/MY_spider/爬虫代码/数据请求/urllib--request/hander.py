import urllib.request

url="http://www.baidu.com"
#创建自己的处理器
handler = urllib.request.HTTPHandler()
#创建自己的opener
opener = urllib.request.build_opener(handler)
#用自己创建的opener调用open方法请求数据
response = opener.open(url)
print(response.read().decode("utf-8"))

#  HTTPHandler还不能去做代理IP
