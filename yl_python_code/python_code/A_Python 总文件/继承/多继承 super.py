class Parent(object):
    def __init__(self, name, *args, **kwargs):   # 为避免多继承报错使用不定长参数接受参数
        print('Parent init执行开始')
        self.name = name
        print('Parent init执行结束')

class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):   # 为避免多继承报错使用不定长参数接受参数
        print('Son1 init执行开始')
        self.age = age
        super().__init__(name, age, *args, **kwargs)   # 为避免多继承报错使用不定长参数接受参数
        print('Son1 init执行结束')

class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):   # 为避免多继承报错使用不定长参数接受参数
        print('Son2 init执行开始')
        self.gender = gender
        super().__init__(name, *args, **kwargs)   # 为避免多继承报错使用不定长参数接受参数
        print('Son2 init执行结束')

class Grandson(Son1,Son2):
    def __init__(self, name, age, gender):
        print('Grandson init执行开始')
        # super(Grandson, self).__init__(name, age, gender)
        # super(Son1, self).__init__(name, age, gender)
        super().__init__(name, age, gender)
        print('Grandson init执行结束')

print(Grandson.__mro__)

gs = Grandson('lihua', 12, 'nan')
print(gs.name)
print(gs.age)
print(gs.gender)

# 继承的时候写 父类名.父类方法 最简单  但是搞不好就会把最高父类调用多次
# P算法能保证之后每个类只会被调用一次的算法
# print(Grandson.__mro__)  python3 里面有一个C3算法来处理多继承时候的调用顺序  C3
# (<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)
# 返回元组  元组里面的顺序决定的调用的顺序
# 如果super（）里面不写参数就会默认的把当前类名作为参数传入 super就会调用元组里面当前类名后面类名里面的方法
# 如果super（）写了参数就会去元组里面找当前参数的后面一个类 去调用当前参数后面一个类里面的方法