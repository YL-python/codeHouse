# 使用自造的cookies登录药智网

import requests

data={
'username': '既见君子1102',
'pwd': '5952768yl'
}


headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

logined_url = 'https://www.yaozh.com/login'

response = requests.post(logined_url, headers=headers, data=data)
print(response.status_code)
with open('text.html','w',encoding='utf-8')  as f:
    f.write(response.content.decode('utf-8'))