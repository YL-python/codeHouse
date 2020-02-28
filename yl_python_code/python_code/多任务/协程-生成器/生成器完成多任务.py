import time

def text1():
    while True:
        print('---1---')
        time.sleep(0.1)
        yield

def text2():
    while True:
        print('---2---')
        time.sleep(0.1)
        yield

def main():
    t1 = text1()
    t2 = text2()
    while True:
        next(t1)
        next(t2)

if __name__ == '__main__':
    main()

# 协程占用资源最少