import urllib.request

url="https://ilovefishc.com/"
proxy = {
    "http":"http://183.63.101.62:53281"
    }

#创建代理的处理器
Proxy_handler = urllib.request.ProxyHandler(proxy)
#创建自己的opener
opener = urllib.request.build_opener(Proxy_handler)
#拿着代理IP调用opener.open()方法请求数据
response = opener.open(url)
t=response.read().decode()
print(t)
