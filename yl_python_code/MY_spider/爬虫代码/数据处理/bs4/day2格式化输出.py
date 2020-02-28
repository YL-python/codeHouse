from bs4 import BeautifulSoup

html_doc = """
<html><head><title id = "one">The Dormouse's story</title></head>
<body>
<p class="story"><!--...--></p>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

"""   #这个网页代码不完整

soup = BeautifulSoup(html_doc,'lxml')

#   wallhaven_spider. 把网页代码补全 格式化输出
result = soup.prettify()
print(result)
