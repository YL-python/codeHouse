 # 名字重整
class Text:
    def __init__(self,name):
        self.__name = name

a = Text('lihua')
try:
    print(a.__name)
except:
    print("获取不到__name属性")
print(a.__dict__)
print(a._Text__name)