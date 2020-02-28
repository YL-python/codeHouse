import urllib.request
import fake_useragent
import re

# 爬取之前，手动打开这个网页，重定向到新的网页，在复制替换
web = 'https://www.915cf.com'

user_agent = fake_useragent.UserAgent()


# 爬取中文有码
def chinese_yes_code(page):
    link = web + '//shipin/list-%E4%B8%AD%E6%96%87%E5%AD%97%E5%B9%95-{0}.html'.format(page)
    headers = {"User-Agent": user_agent.random}
    request = urllib.request.Request(url=link, headers=headers)
    response = urllib.request.urlopen(request)
    info = response.read().decode()
    message = re.findall(r' <a href="(.+)" title="(.+)" target="_blank">', info)
    return message


# 下载迅雷链接
def thunders(urls):
    headers = {"User-Agent": user_agent.random}
    for url, name in urls:
        url = web + url
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        info = response.read().decode()
        thunder = re.search(r'thunder://(.+)" c', info)
        thunder = thunder.group()[0:-3]
        print(thunder)
        store((url, '\t' + name + '\t', thunder + '\n'))


# 保存
def store(message):
    f = open(file='./kitty.txt', mode='a', encoding='utf-8')
    f.writelines(message)
    f.flush()
    f.close()


if __name__ == '__main__':
    total_page = list()
    for p in range(1, 27):
        m = chinese_yes_code(p)
        print('爬取完第{0}个网页'.format(p))
        total_page.extend(m)
    thunders(total_page)
