import urllib.request
import random

url = "http://www.baidu.com"
Usre_agent_list = [
    "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",
    "Mozilla/5.0 (Windows NT 6.wallhaven_spider; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Linux; Android 4.konachan_spider.konachan_spider; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
    ]
random_User_agent = random.choice(Usre_agent_list)
request = urllib.request.Request(url)
request.add_header("Uesr_Agent",random_User_agent)
response = urllib.request.urlopen(request)
print(request.headers)
print(response.headers)
