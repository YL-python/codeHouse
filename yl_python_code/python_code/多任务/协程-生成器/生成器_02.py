def Fibo(all_num):
    print('---1---')
    a, b = 0, 1
    index_num = 0
    while index_num <= all_num:
        print('---2---')
        yield a
        print('---3---')
        a, b = b, a+b
        index_num += 1
        print('---4---')

# 如果一个函数里面有 yield 函数就不叫函数就会变成生成器模板
# 调用的函数里面有 yield 的时候对象就会变成生成器对象
# 不管是next方法还是for语句调用到生成器的时候每次生成器执行到yield的时候会暂停 不是结束这个函数
# 下一次调用的时候就从暂停的地方继续

obj = Fibo(2)
print(next(obj))
print(next(obj))

# for i in obj :
#     print(i)