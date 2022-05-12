from multiprocessing import Process, Lock
from time import sleep
from random import random


def func(num: int, lock: Lock):
    lock.acquire()
    print("Блокировка!")
    with open("locker.txt", "a") as f_o:
        print("Новая строка в файл", num)
        f_o.write(f"{num}\n")
    lock.release()


if __name__ == "__main__":
    lock = Lock()
    p = Process(target=func, args=(0, lock))
    p1 = Process(target=func, args=(1, lock))
    p2 = Process(target=func, args=(2, lock))
    p3 = Process(target=func, args=(3, lock))
    p4 = Process(target=func, args=(4, lock))
    p5 = Process(target=func, args=(5, lock))
    p6 = Process(target=func, args=(6, lock))
    p.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p.join()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()