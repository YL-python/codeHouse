# 使用自造的cookies登录马蜂窝

import requests
from lxml import etree

str = 'mfw_uuid=5cde6afb-8926-977a-fb48-93ddd72a2369; _r=baidu; _rp=a%3A2%3A%7Bs%3A1%3A%22p%22%3Bs%3A18%3A%22www.baidu.com%2Flink%22%3Bs%3A1%3A%22t%22%3Bi%3A1558080251%3B%7D; __mfwothchid=referrer%7Cwww.baidu.com; __mfwlv=1558080247; __mfwvn=konachan_spider; uva=s%3A264%3A%22a%3A4%3A%7Bs%3A13%3A%22host_pre_time%22%3Bs%3A10%3A%222019-05-17%22%3Bs%3A2%3A%22lt%22%3Bi%3A1558080251%3Bs%3A10%3A%22last_refer%22%3Bs%3A137%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DwZcpYEQ3GCQzDH1Y0zPesOs6cEW4yv5dGr8TR7mOxQfzwr-hajvW0ecBNctCJwcU%26wd%3D%26eqid%3Db9b0bb180000e5fd000000065cde6af6%22%3Bs%3A5%3A%22rhost%22%3Bs%3A13%3A%22www.baidu.com%22%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1558080251%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A13%3A%22www.baidu.com%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=5cde6afb-8926-977a-fb48-93ddd72a2369; UM_distinctid=16ac4d1d99321c-07db8797a37439-3b654406-144000-16ac4d1d9944d0; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222019-05-17+16%3A05%3A46%22%3B%7D; uol_throttle=50399262; PHPSESSID=n10gco644hrbevfb13lun38hg7; __mfwlt=1558081416'

str_list = str.split(';')

# print(str_list)

cookies = {}

for item in str_list:
    # print(item)
    key = item.split('=')[0].strip()
    value = item.split('=')[1].strip()
    cookies[key] = value
print(cookies)

header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

logined_url = 'http://www.mafengwo.cn/friend/index/follow?uid=70360114'
response = requests.get(logined_url, headers=header, cookies=cookies)
print(response.status_code)

tree = etree.HTML(response.text)

friends = tree.xpath('//div[@class="name"]/a/text()')
print(friends)