import time
from multiprocessing import Queue, Pipe, Pool
from time import sleep


def worker(a: int, q: Queue):
    cnt = 0
    while cnt < 3:
        sleep(1)  # какое-то долгое вычисление
        print(a)
        cnt += 1
        q.put(a)


def pipe_worker(p: Pipe):
    some_data = input("Введите данные: ")
    p.send(some_data)


def sleepy_printer(a):
    print("I'm sleeping")
    time.sleep(30)
    print(a)


def f(a):
    return a + a


if __name__ == "__main__":
    # q = Queue(maxsize=100)
    # p = Process(target=worker, args=(1, q))
    # p.start()
    # p1 = Process(target=worker, args=(2, q))
    # p1.start()
    # p1.join()
    # p.join()
    # print("24 result", q.get())
    # print("25 result", q.get())
    # print("26 result", q.get())
    # print("27 result", q.get())
    # print("28 result", q.get())
    # print("29 result", q.get())
    # parent_pipe, child_pipe = Pipe()
    # pipe_worker(child_pipe)
    # print("Информация из дочернего процесса:", parent_pipe.recv())
    pass