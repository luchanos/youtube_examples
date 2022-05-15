from multiprocessing import Pipe, Process


def pipe_worker(p: Pipe):
    some_data = 100500
    p.send(some_data)


def pipe_worker_2(p: Pipe):
    print("!!!", p.send(111))


if __name__ == "__main__":
    # работаем с конвейерами
    parent_pipe, child_pipe = Pipe()
    p = Process(target=pipe_worker, args=(child_pipe, ))
    p.start()
    p1 = Process(target=pipe_worker_2, args=(child_pipe,))
    p1.start()
    print("Информация из дочернего процесса:", parent_pipe.recv())
    parent_pipe.send("Информация из главного процесса")
    p.join()
    p1.join()
