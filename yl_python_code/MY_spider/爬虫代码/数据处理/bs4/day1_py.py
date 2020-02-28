from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""   #这个网页代码不完整

#konachan_spider. 转解析类型
#   默认的 bs4 会调用当前系统的 lxml 的解析库 就会报警告
#   传第二个参数就可以主动设置 bs4 的解析库
soup = BeautifulSoup(html_doc,'lxml')   # 转成 lxml 类型 指定解析库

#   wallhaven_spider. 把网页代码补全 格式化输出
result = soup.prettify()
print(result)

#3. 解析数据 取标签内容（.标签名）  .(点)操作  .p 就是取 p标签内容
''' 但是点操作只能取到同名标签的第一个标签 '''
#   result = soup.head
#   print(result)
#   result = soup.p
#   print(result)

#4. 取文本（.string）  同名标签只能取到第一个
#   result = soup.p.string
#   print(result)

#5. 取属性（.标签[属性]）取某标签的某属性
result = soup.a['href']
print(result)
result = soup.p['class']
print(result)
