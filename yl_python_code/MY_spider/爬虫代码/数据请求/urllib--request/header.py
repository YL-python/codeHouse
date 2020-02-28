import urllib.request
import urllib.parse
import string

url="https://www.baidu.com"

request = urllib.request.Request(url)#创建请求对象 请求网络数据

responce = urllib.request.urlopen(request)#返回网络数据 (二进制“utf-8”)

print(request.headers,end= "\n\n\n")#打印请求头信息
#结果为空  因为我们还没有向请求对象内输入数据

print(responce.headers)#打印响应头信息

