# class Foo:
# #     def get_bar(self):
# #         return 'lihua'
# #
# #     BAR = property(get_bar)   # 只传方法名 不加括号
# #
# # obj = Foo()
# # result = obj.BAR
# # print(result)

# property 方法有四个参数 前三个参数传方法名第四个参数传解释文档
# 第一个定义函数 调用对象.属性 自动触发
# 第二个修改函数 调用对象.属性=XXX 自动触发
# 第三个删除函数 调用del自动触发
# 对象.属性.__doc__ 调用解释文档

class Foo:
    NAME = 'lihua'
    def Get_bar(self):
        print('Get_bar调用')
        return self.NAME

    def Set_bar(self,value):
        print('Set_bar调用')
        self.NAME = value
        return self.NAME

    def Del_bar(self):
        print('Del_bar调用')
        del self.NAME

    BAR = property(Get_bar,Set_bar,Del_bar,'这个是解释文档。。。')


obj = Foo()
result = obj.BAR
print(result)
obj.BAR = 'xiaomin'
print(obj.BAR)
desc = Foo.BAR.__doc__
print(desc)
del obj.BAR
print(obj.BAR)