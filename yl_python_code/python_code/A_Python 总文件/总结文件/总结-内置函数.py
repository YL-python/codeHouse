# 返回x的十六进制  hex()
x = 123456789
print(hex(x))


# 返回x的8进制   oct(x)
print(oct(x))


# 接收两个数字类型（非复数）参数，返回一个包含商和余数的元组(a // b, a % b)
x,y = divmod(10,3)
print(x,y)


# id() 函数用于获取对象的内存地址。
print(id(x))


# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
print(sorted([1,2,8,4,5,7,4,7],reverse=False))             # reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。


# enumerate(sequence, [start=0]) 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
x = [1,2,'yl','python']
print('普通for'.center(10,'-'))
for i in x:
    print(i)
print('enumerate for'.center(20,'-'))
for i,j in enumerate(x,start=1):
    print(i,j)


# any()