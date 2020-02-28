from collections import Iterable
from collections import Iterator

# 迭代器可以用  for 循环


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.index = 0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.names):
            ret = self.names[self.index]
            self.index += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add('张三')
classmate.add('李四')
classmate.add('王二')
classmate.add('麻子')

# print("判断classmate是否是可迭代对象：", isinstance(classmate,Iterable))
# classmate_iterator = iter(classmate)
# print("判断classmate_iterator是否是可迭代对象：", isinstance(classmate_iterator,Iterable))

for i in classmate:
    print(i)