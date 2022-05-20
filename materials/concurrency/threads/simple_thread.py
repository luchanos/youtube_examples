import time
from threading import Thread
from time import sleep
import threading
import os
from datetime import datetime


def func_heavy_math():
    """Функция с тяжелыми вычислениями"""
    cnt = 0
    # какая-то математическая тяжёлая операция
    for _ in range(500_000_000):
        cnt += 1
    print(f"Это поток {threading.get_ident()} из процесса {os.getpid()}")


def func_sleep():
    """Функция с имитацией I/O bound операции"""
    time.sleep(1)


start_time = datetime.now()
th1 = Thread(target=func_sleep)
th2 = Thread(target=func_sleep)
th1.start()
th2.start()
th2.join()
th1.join()
print(f"Total time for execution of function is {datetime.now() - start_time}")
