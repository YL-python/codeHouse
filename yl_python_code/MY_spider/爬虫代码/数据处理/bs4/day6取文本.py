from bs4 import BeautifulSoup

html_doc = """
<html><head><title id = "one">The Dormouse's story</title></head>
<body>
<p class="story"><!--...--></p>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" cl ass="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

"""

soup = BeautifulSoup(html_doc,'lxml')

#取标签包裹的内容
result = soup.select('a')[1].get_text()
print(result)

#取标签的属性
result = soup.select('#link1')[0].get('href')
print(result)
