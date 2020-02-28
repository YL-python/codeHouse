def text1(a, b, *arg, **kwargs):   # 这里的* **表示接受不定长参数 *是接受参数 元组表示，**是 接受关键字参数 字典表
    print("text1".center(20,'*'))
    print(a)
    print(b)
    print(arg)
    print(kwargs)
    text2(a ,b ,arg, kwargs)
    text3(a, b, *arg, **kwargs)   # 这里的* ** 表示解压

def text2(a, b, *arg, **kwargs):
    print("text2".center(20,'*'))
    print(a)
    print(b)
    print(arg)
    print(kwargs)

def text3(a, b, *arg, **kwargs):
    print("text3".center(20,'*'))
    print(a)
    print(b)
    print(arg)
    print(kwargs)

text1(11,22,3,44,name = 'lihua', age = 55)

def text4(c):
    print("text4".center(20,'*'))
    print(c)
    print(*c)

text4((1,2,3))