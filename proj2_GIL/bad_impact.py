from threading import Thread
from time import time

NUMBER = 10**8


def count(num: int):
    while num > 0:
        num -= 1


start = time()
t1 = Thread(target=count, args=(NUMBER // 2,))
t2 = Thread(target=count, args=(NUMBER // 2,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time()
print("Run time: ", end - start)
