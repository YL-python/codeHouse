import multiprocessing
def text():
    while True:
        pass

t1 = multiprocessing.Process(target=text)
t1.start()
while True:
    pass