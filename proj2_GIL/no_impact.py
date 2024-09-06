from threading import Thread
from time import time, sleep

NUMBER = 100


def wait(millis: int):
    for i in range(millis):
        sleep(0.01)


# Multi-threaded
t1 = Thread(target=wait, args=(NUMBER,))
t2 = Thread(target=wait, args=(NUMBER,))
start = time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time()

# Single-threaded
start = time()
wait(NUMBER)
end = time()

print("Run time: ", end - start)
