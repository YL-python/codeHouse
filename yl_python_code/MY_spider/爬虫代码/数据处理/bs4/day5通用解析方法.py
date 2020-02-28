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

"""
#转解析类型
soup = BeautifulSoup(html_doc, 'lxml')

#通用解析方法

#   find(name,attrs)---返回找到的第一个
print('-------------find(name,attrs)--------------------------')
result = soup.find(name = 'p')   #标签名称查找
print(result)
result = soup.find(attrs={'class':"title"})   #属性查找
print(result)
result = soup.find('p')   
print(result)
result = soup.find({'class':"title"})   
print(result)
#传一个参数时默认为name的参数
print('-------------------------------------------------------')

#   find_all(name,attrs,limit)   返回列表（标签对象）
print('--------------find_all(name,attrs,limit)---------------')
result = soup.find_all(name = 'p')   #标签名称查找
print(result)
result = soup.find_all(attrs={'class':"sister"})   #属性查找
print(result)
result = soup.find_all(name = 'p',limit = 1)   #limit限制找几个
print(result)
print('-------------------------------------------------------')

#   select_one()---css的选择器  返回值是列表
print('--------------select_one()-----------------------------')
result = soup.select_one('.sister')
print(result)
print('-------------------------------------------------------')

#   select---css的选择器   返回值是列表
print('--------------select()---------------------------------')
result = soup.select('p')   #标签选择器
print(result)
result = soup.select('.sister')  #类选择器  .  与class关联
print(result)
result = soup.select('#link1')   #id选择器  #  与id关联
print(result)
result = soup.select('head title')   #后代选择器  找head的后代title
print(result)
result = soup.select('title, .title')   #组选择器 组合选择器  这里是（标签加类 选择器）
print(result)
result = soup.select('a[id="link3"]')   #属性选择器
print(result)
print('-------------------------------------------------------')
