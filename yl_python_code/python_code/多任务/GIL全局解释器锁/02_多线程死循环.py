import threading

def text():
    while True:
        pass

t1 = threading.Thread(target=text)
t1.start()
while True:
       pass