from lxml import etree
import requests
import re

#定义一个头部信息，模仿头部
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.konachan_spider; WOW64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/65.0.3325.181 Safari/537.36"
}
#这是连接url
CTION = "https://www.dytt8.net"
#这里是取出页面里面的 内容 /html/gndy/dyzz/20190822/59011
def get_url_The(url):
    #发送请求
    response = requests.get(url,headers=HEADERS)
    #print(response)#状态吗 200 成功

    #解压成text元素
    text = response.content.decode("gbk","ignore")
    # print(text)

    # The_title = re.findall(r'<div class="co_content8">.*?<a href="(.*?)" '
    #                        r'class="ulink">.*?</a>',text,re.S)
    # 解压完之后，再取里面的内容
    The_title = re.findall(r"/html/gndy/dyzz/\d+.*?\d+.html",text,re.S)
    # print(The_title)
    #print(The_title)
    # for The in The_title:
    #     print(connection + The)
    # 这里可以用匿名函数操作输出一个完整的url 得到的内容的url加上头部的 https://www.dytt8.net 变成一个完整url
    anonymous = map(lambda title:CTION + title,The_title)

    #https://www.dytt8.net/html/gndy/dyzz/20190819/59004.html 返回一个列表
    return anonymous

#这里是输出第一页url里面的内容
def details_url(url):
    #发送请求
    response = requests.get(url,headers=HEADERS)
    #解压成text元素，需要手动解码
    text = response.content.decode("gbk","ignore")
    # print(text)
    #在之后取出需要的内容
    THE_title = re.findall(r'<div class="title_all"><h1><font color=#07519a>(.*?)</font>',text,re.S)

    print(THE_title)


#这里是循环输出页面
def starting():
    # 首先定义一个url
    get_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    #这个循环用来输入页面的url
    for i in range(1,8):
        cycle = get_url.format(i)
        # 这里输出的是多少页，输出多少页之后再把页数的url传递给get_url_The函数去解析内容
        # print(cycle)
        datail_urls = get_url_The(cycle)
        #这个循环用来解析第一页的每个url详情
        for details in datail_urls:#https://www.dytt8.net/html/gndy/dyzz/20190819/59004.html
            # print(details)
            #在传递给starting函数去解析里面的内容
            parsing = details_url(details)
            break
        break


#当作是主函数直接调用其他函数就行
if __name__ == '__main__':
    starting()
