class Parent(object):
    def __init__(self,name):
        print('Parent init执行开始')
        self.name = name
        print('Parent init执行结束')


class Son1(Parent):
    def __init__(self, name, age):
        print('Son1 init执行开始')
        self.age = age
        Parent.__init__(self,name)
        print('Son1 init执行结束')

class Son2(Parent):
    def __init__(self, name, gender):
        print('Son2 init执行开始')
        self.gender = gender
        Parent.__init__(self,name)
        print('Son2 init执行结束')

class Grandson(Son1,Son2):
    def __init__(self, name, age, gender):
        print('Grandson init执行开始')
        self.name = name
        Son1.__init__(self, name, age)
        Son2.__init__(self, name, gender)
        print('Grandson init执行结束')

gs = Grandson('lihua', 12, 'nan')
print(gs.name)
print(gs.age)
print(gs.gender)

# 像这种在继承的时候写 父类.父类方法 会导致最高的父类被调用多次 者并不是我们希望的