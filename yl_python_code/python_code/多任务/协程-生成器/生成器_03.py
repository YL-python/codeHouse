def Fibo(all_num):
    a, b = 0, 1
    index_num = 0
    while index_num <= all_num:
        yield a
        a, b = b, a+b
        index_num += 1

    return 'ok---'

obj = Fibo(4)

while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as ret :
        print(ret.value)
        break

# 想取生成器的返回值 要在最后异常处理的时候 因为return是在最后才执行的