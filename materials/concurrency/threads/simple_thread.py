import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from time import sleep
import threading
import os
from datetime import datetime
CNT = 0


def func_heavy_math():
    """Функция с тяжелыми вычислениями"""
    cnt = 0
    # какая-то математическая тяжёлая операция
    for _ in range(50_000_000):
        cnt += 1
    print(f"Это поток {threading.get_ident()} из процесса {os.getpid()}")


def func_sleep():
    """Функция с имитацией I/O bound операции"""
    print(f"Это поток {threading.get_ident()} из процесса {os.getpid()}")
    time.sleep(1)


def func_cnt_printer_and_incrementer():
    global CNT
    CNT += 1
    print(f"Это поток {threading.get_ident()} из процесса {os.getpid()}: {CNT}")


start_time = datetime.now()
# th1 = Thread(target=func_heavy_math)
# th2 = Thread(target=func_heavy_math)
# th3 = Thread(target=func_heavy_math)

# with ThreadPoolExecutor(max_workers=2) as t:
#     [t.submit(func_heavy_math) for _ in range(3)]

# th1.start()
# th2.start()
# th3.start()
# th3.join()
# th2.join()
# th1.join()
func_heavy_math()
func_heavy_math()
func_heavy_math()
print(f"Total time for execution of function is {datetime.now() - start_time}")
