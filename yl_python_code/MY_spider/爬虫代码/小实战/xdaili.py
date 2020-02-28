import json
import requests
import random

def crawl_xdaili():
    """
    获取讯代理
    :return: 代理
    """

    # url = 'http://api.xedl.321194.com/getip?num=2&type=2&port=11&pack=2024&ts=0&cs=1&lb=2'#2个
    url = 'http://api.xedl.321194.com/getip?num=1&type=2&port=1&pack=3975&ts=0&cs=1&lb=2'#1个 #num = wallhaven_spider
    result = requests.get(url)#api获取
    # print(result.text)#产物是str
    # print(type(result.text))#json.loads产物是str
    # print(result.json())#调用 json()方法，就可以将返回结果是 JSON 格式的字符串转化为字典
    proxies = result.json().get('data')
    # print(proxies)
    # print(type(proxies))#list [{'ip': '58.218.200.223', 'port': 30762,......
    for proxy in proxies:
        yield proxy['ip']+':'+str(proxy['port'])

def get_one():
#非常好的while True,不产出None
    while True:
        try:
            results = list(crawl_xdaili())
            result = random.choices(results)
            if result != []:
                return result[0]
                break
        except:
            pass




if __name__ == "__main__":
    for i in range(100):
        print(get_one())




