'''
这里用来写字符串的使用方法的呀
'''
# 1 下标可以访问字符串的值
print('1、下标可以访问字符串的值'.center(50,'-'))
str1='0123456789abcdefg'
print('str1 = ',str1)
print('str1[1] = ',str1[1])
print('str1[0:5] = ',str1[0:5])
print('str1[0:15:2] = ',str1[0:15:2])  #  开始：结束：步长

print()

'''
2、转义字符
\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\b	退格(Backspace)
\n	换行
\t	横向制表符
\r	回车
\f	换页
\\oyy	八进制数，yy 代表的字符，例如：\o12 代表换行，其中 o 是字母，不是数字 0。
\\xyy   十六进制数，yy代表的字符，例如：\x0a代表换行
\other	其它的字符以普通格式输出
'''

print('2、字符串的运算符'.center(50,'-'))
a='Hello'
b='Python'
print('a = %s   '%a,'b = %s'%b)
print('加法  + ：',end='')
print('a+b = ',a+b)
print('乘法  * ：',end='')
print('a*3 = ',a*3)
print('判断  in  ，not in：')
print('\'He\' in a = ', 'He'in a)
print('\'He\' not in a = ', 'He'not in a)
print('r/R可以输出原始字符串的内容：')
print(r'\n\\\n\'\'\'')
print(R'\n\\\n\'\'\'')
print()


'''
字符串的格式化符号
%c	 格式化字符及其ASCII码
%s	 格式化字符串
%d	 格式化整数
%u	 格式化无符号整型
%o	 格式化无符号八进制数
%x	 格式化无符号十六进制数
%X	 格式化无符号十六进制数（大写）
%f	 格式化浮点数字，可指定小数点后的精度
%e	 用科学计数法格式化浮点数
%E	 作用同%e，用科学计数法格式化浮点数
%g	 %f和%e的简写
%G	 %f 和 %E 的简写
%p	 用十六进制数格式化变量的地址
'''

print('3、字符串常用函数'.center(50,'-'))

# 居中对齐函数   center(width, fillchar) 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
print('\'python\'.center(20,"*")：%s'%('python'.center(20,'*')))

# 左右对齐函数  ljust/rjust(width, fillchar)
print('\'python\'.ljust(20,"*")：%s'%('python'.ljust(20,'*')))
print('\'python\'.rjust(20,"*")：%s'%('python'.rjust(20,'*')))

# 搜索函数  str.find(str, beg=0, end=len(string):检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
print('\'nihao\'.find("i",2)：%s'%('nihao'.find('i',2)))

# 字符串替换  str.replace(old, new[, max])
print('\'1 2 3 4 5 6\'.replace(\' \',\'\',3)：%s'%('1 2 3 4 5 6'.replace(' ','',3)))

# 字符串切片   str.split(str="", num=string.count(str))   分割次数默认 最大
print('\'text.txt\'.split(".")：%s'%('text.txt'.split('.')))

# 把可迭代对象用指定字符串连接   str.join(iterable)  字符串 列表 元组 字典
print("'-'.join(['p','y','t','h','o','n']) ：%s"%('-'.join(['p','y','t','h','o','n'])))

'''
capitalize()  *将字符串的第一个字符转换为大写

isalpha() *字符串是  纯字母  就返回 True, 否则返回 False
	
isdigit()  *如果字符串  只包含数字  则返回 True 否则返回 False..
	
isspace()   *如果字符串中  只包含空白，则返回 True，否则返回 False.
	
len(string)   *返回字符串长度
	
lower()   *字符串中所有大写字符转换为小写.  大写转小写
	
upper()  *字符串中的小写字母转换为大写      小写转大写

swapcase()  *将字符串中大写转换为小写，小写转换为大写

max(str)  返回字符串 str 中最大的字母。
min(str)  返回字符串 str 中最小的字母。

count(str, beg= 0,end=len(string))  *返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

encode(encoding='UTF-8',errors='strict')  *以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

bytes.decode(encoding="utf-8", errors="strict")  *Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。

endswith(suffix, beg=0, end=len(string))   *检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
	
index(str, beg=0, end=len(string))  *跟find()方法一样，只不过如果str不在字符串中会报一个异常.
'''