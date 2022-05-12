from multiprocessing import Process
from time import sleep


def func(a):
    cnt = 0
    while True:
        sleep(1)
        print(a)
        cnt += 1
        if cnt > 2:
            break


if __name__ == "__main__":
    p = Process(target=func, args=(1, ))
    p.start()
    p1 = Process(target=func, args=(2, ))
    p1.start()
