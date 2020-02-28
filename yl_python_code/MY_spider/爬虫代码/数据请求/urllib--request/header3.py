# wallhaven_spider.动态加请求头方式
import urllib.request as a
import urllib.parse

url='http://ilovefishc.com/'

head={"User-Agent":"Mozilla/5.0 (Windows NT 6.konachan_spider; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

request = a.Request(url)

request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.konachan_spider; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
#动态添加请求头

response = a.urlopen(request)


print(request.headers)

print(response.read().decode())


