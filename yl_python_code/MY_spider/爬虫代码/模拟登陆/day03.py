# 利用cookies登录马蜂窝

import requests
from lxml import etree

# session相当于构造一个用户来记录数据   session.cookies   方法来获取cookies

session = requests.Session()
phone_number = '15170915459'
password = '5952768yl'
data = {'passport': phone_number, 'password': password}
header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

r = session.post("https://passport.mafengwo.cn/login/", headers=header, data=data)

cookies = session.cookies
# print(cookies)
print(cookies.get_dict())

# print(r.status_code)
# # print(r.text)
#
logined_url = 'http://www.mafengwo.cn/friend/index/follow?uid=70360114'
response = requests.get(logined_url, headers=header, cookies=cookies)
print(response.status_code)

tree = etree.HTML(response.text)
#
friends = tree.xpath('//div[@class="name"]/a/text()')
print(friends)