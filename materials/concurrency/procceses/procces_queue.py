from multiprocessing import Queue, Pipe, Process
from time import sleep


def worker(a: int, q: Queue):
    cnt = 0
    while cnt < 3:
        sleep(1)  # какое-то долгое вычисление
        print(a)
        cnt += 1
        q.put(a)


def pipe_worker(p: Pipe):
    some_data = 100500
    p.send(some_data)


def pipe_worker_2(p: Pipe):
    print(p.recv())


def f(a):
    return a + a


if __name__ == "__main__":
    # работаем с очередями
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

    # работаем с конвейерами
    parent_pipe, child_pipe = Pipe(duplex=True)
    p = Process(target=pipe_worker, args=(child_pipe, ))
    p.start()
    p1 = Process(target=pipe_worker_2, args=(child_pipe, ))
    p1.start()
    print("Информация из дочернего процесса:", parent_pipe.recv())
    parent_pipe.send("Информация из главного процесса")
    p.join()
    p1.join()
