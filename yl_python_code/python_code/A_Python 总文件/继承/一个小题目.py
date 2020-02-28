class Parent(object):
    x = 1


class Son1(Parent):
    pass


class Son2(Parent):
    pass

print(Parent.x, Son1.x, Son2.x)   # Son1.x Son2.x 是去找父类的参数
Son1.x = 2
print(Parent.x, Son1.x, Son2.x)   # Son1.x = 2 是给Son1添加了一个参数 Son2.x 是去找父类的参数
Parent.x = 3
print(Parent.x, Son1.x, Son2.x)   # x 先会去找本身是否有这个参数 没有再去父类里面找