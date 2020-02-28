import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()

headers = {
    "USer-Agent" : ua.random
}
text_url = 'https://www.baidu.com/'
with open('ip.text','a',encoding = 'utf-8')as f:
    for x in range (1,11):
        url = 'https://www.xicidaili.com/nn/'+str(x)
        html = requests.get(url, headers=headers).content.decode()
        soup = BeautifulSoup(html, 'lxml')
        all = soup.find_all('tr', class_='odd')
        for i in all:
            t = i.find_all('td')
            ip = t[1].text+":"+t[2].text
            proxies = {'http' : 'http'+'\\'+ip,'https' : 'https'+'\\'+ip}  #构建IP
            try:
                respone = requests.get(text_url,proxies=proxies,headers = headers,timeout = 5).status_code# 请求
                if respone == 200:      #查看请求结果
                    f.write(proxies+"\n")
                    print(proxies)
            except:
                print("error")

