"""
Процессы общаются между собой с помощью очередей и конвейеров. Что применять - зависит от типа задачи.

Семафор - штука, которая позволяет защитить доступ к ресурсам.

Очереди - великолепный способ отправки небольших данных от или к множеству процессов.
"""
from datetime import datetime
from multiprocessing import Process, Queue
import os
from random import randint


# def f(q):
#     print(q.get())
#     pid = os.getpid()
#     q.put(f"Hello from {pid}")


# if __name__ == '__main__':
#     q = Queue()
#     q.put("Привет из родительского процесса!")
#     q.put("Привет из родительского процесса 2!")
#     q.put("Привет из родительского процесса 2!")
#     p = Process(target=f, args=(q,))  # целевая функция - f, в качестве аргумента она принимает очередь
#     p_1 = Process(target=f, args=(q, ))
#     p.start()
#     p_1.start()
#     print(q.get())    # достали объект из очереди, по сути из дочернего процесса
#     print(q.get())
#     # print(q.get())  # будет ждать, что мы что-то положим. Пока не положим - дальше не пойдёт
#     # print(q.get())
#     p.join()


# def laborator(q: Queue):
#     result = 0
#     with open("file.txt", "r") as f_o:
#         for s in f_o:
#             # pass
#             result += randint(0, int(s))  # именно на эту строчку будут приходиться основные расходы
#     print(os.getpid(), result)
#     q.put(result)


# # Пример с нашим чтецом файла
# if __name__ == "__main__":
#     start = datetime.now()
#     q = Queue()  # создаём наш "портал"
#     p_list = [Process(target=laborator, args=(q, )) for _ in range(2)]
#     for p in p_list:
#         p.start()
#     for p in p_list:  # без этого основной поток завершит работу, но это не помешает работать дочерним
#         p.join()
#     res = q.get() + q.get()  # тащим данные из "портала"
#     print(res)
#     print(datetime.now() - start)


from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  # создаём как бы 2 стороны кротовьей норы
    p = Process(target=f, args=(child_conn,))  # отдаём 1 сторону в процесс
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()

# надо быть осторожным с Pipe, потому что данные могут развалиться, если 2 процесса одновременно начнут
# в него писать