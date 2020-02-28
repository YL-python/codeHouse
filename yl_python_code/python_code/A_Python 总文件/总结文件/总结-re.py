import re
# re.findall(p,str)
# re.compile(p)
# re.sub(old p,new str,str)

str = '<p>asdfghj   kl</p>'  # \t \n 123 -[]/\ 你好

# 通配符  （.*？）
p = re.compile('<p>(.*?)</p>')
data = p.findall(str)
# print(data)
# 注意 这里 . 不能匹配 \n 要让 . 能匹配 \n 需要写成一下形式
# p = re.compile('<p>(.*?)</p>'，re.S)  或者 p = re.compile('<p>(.*?)</p>'，re.DOTALL)

# re匹配空
str = '<p>asdfghj  \t \n 123 -[]/\ 你好  kl</p>'
data = re.sub(r"[\s]", '',str)
print(data)

