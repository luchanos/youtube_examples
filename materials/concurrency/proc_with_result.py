from multiprocessing import Process, Queue, Pipe
from time import sleep


def laborator():
    sleep(3)


def f(q):
    q.put([42, None, 'hello'])


if __name__ == "__main__":
    q = Queue()
    p = Process(target=f, args=(q,))  # передали очередь в качестве аргумента
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()
