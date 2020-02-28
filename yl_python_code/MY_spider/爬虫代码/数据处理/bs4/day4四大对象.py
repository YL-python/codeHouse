from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story"><!--...--></p>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

"""
#第一个p标签的内容是注释

soup = BeautifulSoup(html_doc,'lxml')   #是bs4.BeautifulSoup 的对象

#  .(点)操作   点操作只能取同名标签的第一个

#取标签  Tag  标签对象
result = soup.head
print(type(result))

#p.strng 是 Comment  注释内容对象
result = soup.p
print(type(result))
result = soup.p.string
print(type(result))
result = soup.p.string
print(result)

#取标签内容  NavigableString  字符串对象 也是string的一个子类
result = soup.a.string
print(type(result))

#取标签的某个属性
result = soup.p['class']
print(type(result))
result = soup.a['href']
print(type(result))


'''四大对象

Tag
NavigableString
Comment
BeautifulSoup

'''
