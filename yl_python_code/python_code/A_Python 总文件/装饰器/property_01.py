class A:

    def text1(self):
        print('---text1---')
        return 100

    @property
    def text2(self):
        print('---text2---')
        return 100


a = A()
a1_num = a.text1()
a2_num = a.text2
print(a1_num)
print(a2_num)

# 运用 @property  属性定义了一个函数 传参只要传self 调用的时候只要 类对象.方法名 不要括号
# 看上去就像调用了一个类属性 加强了代码的可读性 让人们只要关注他的返回值不用在意他实现的方法
# property 定义的方法不能再传其他参数  类对象.property 相当于是这个方法的返回值 再用括号不能调用到返回值的方法