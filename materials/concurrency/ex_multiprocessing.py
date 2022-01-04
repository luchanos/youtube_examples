# В питон для создания процессов и работы с ними используют модуль multiprocessing
import time
from multiprocessing import Process
import os
CNT = 0


def f_2():
    global CNT
    CNT += 1
    print(f"f_2: {CNT} from", os.getpid())


def f_1():
    global CNT
    CNT += 1
    p = Process(target=f_2, args=())
    p.start()
    print(f"f_1: {CNT} from", os.getpid())


def f():
    global CNT
    CNT += 1
    p = Process(target=f_1, args=())
    p.start()
    print(f"f: {CNT} from", os.getpid())


if __name__ == "__main__":  # выполнится только в главном процессе
    time.sleep(1)
    print(f"{os.getpid()} ENTERED!")
    p = Process(target=f, args=())  # создаём объект, в котором хотим запустить функцию с параметрами
    p.start()  # тут будет под капотом форкнут процесс и в нём выполнена функция с параметрами
    p.join()  # ожидание завершения всех дочерних процессов
    print(f"{os.getpid()} FINISNED!")
    print(f"value = {CNT}")

    # ХОЗЯЙКЕ НА ЗАМЕТКУ: не во всех системах есть системные вызовы fork, поэтому юзать multiprocessing - это хорошо!
    # Все делают за нас!
