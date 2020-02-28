import urllib.request

url="https://ilovefishc.com/"
proxy_list = [
    {"http":"http://183.62:53281"},
    {"http":"http://58.254.220.116:52470"},
    {"http":"http://61.142.72.154:30074"},
    {"http":"http://221.218.102.146:33323"},
    {"http":"http://111.177.168.24:9999"}
    ]
for proxy in proxy_list:
    #print(proxy)
    
    #创建代理的处理器
    Proxy_handler = urllib.request.ProxyHandler(proxy)
    #创建自己的opener
    opener = urllib.request.build_opener(Proxy_handler)
    #拿着代理IP调用opener.open()方法请求数据
    #response = opener.open(url)
    try:
        response = opener.open(url,timeout=1)
        print(response.read().decode("utf-8"))
        print("haha")
    except Exception as e:
        print(e)

    
 
