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
"""

soup = BeautifulSoup(html_doc,'lxml')

#  .(点)操作   点操作只能取同名标签的第一个

#取标签
result = soup.head
print(result)
result = soup.p
print(result)

#取标签内容
result = soup.p.string
print(result)
result = soup.a.string
print(result)

#取标签的某个属性
result = soup.p['class']
print(result)
result = soup.a['href']
print(result)
