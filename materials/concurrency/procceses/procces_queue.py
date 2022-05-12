from multiprocessing import Process, Queue
from time import sleep


def func(a, q):
    cnt = 0
    while True:
        sleep(1)
        print(a)
        cnt += 1
        q.put(a)
        if cnt > 2:
            break


if __name__ == "__main__":
    q = Queue(maxsize=100)
    p = Process(target=func, args=(1, q))
    p.start()
    p1 = Process(target=func, args=(2, q))
    p1.start()
    p1.join()
    p.join()
    print("result", q.get())
