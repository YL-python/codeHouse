def Fibo(all_num):
    a, b = 0, 1
    index_num = 0
    while index_num <= all_num:
        ret = yield a
        print('>>>>ret>>>>',ret)
        a, b = b, a+b
        index_num += 1


obj = Fibo(4)
print(next(obj))
print(next(obj))
print(next(obj))
print(obj.send('hahhah'))

# 向生成器里面传值用send方法  但是send不能放在第一次
# 传值可以在此之后用一些判断来做别的事情