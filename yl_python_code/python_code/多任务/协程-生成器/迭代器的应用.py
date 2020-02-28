# 现在需要一大推 有效值
# 方案一：把值生成好放在内存里面 什么时候要什么时候拿
# 方案二：把生成有效值的方法保存起来 什么时候要 什么时候生成一个

# 迭代器 存储的就是生成数据的方法而不是大量的数据

# 实现斐波那契数列
# 方案一

# nums = list()
# a = 0
# b = 1
# i = 0
# while i < 10:
#     nums.append(a)
#     a , b = b , a + b
#     i += 1
# for i in nums:
#     print(i)

# 方案二
class Fibinacci(object):
    def __init__(self,all_num):
        self.a = 0
        self.b = 1
        self.index = 0
        self.all_num = all_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.all_num:
            ret = self.a
            self.a ,self.b = self.b,self.a+self.b
            self.index+=1
            return ret
        else:
            raise StopIteration

fibo = Fibinacci(10)

for i in fibo:
    print(i)