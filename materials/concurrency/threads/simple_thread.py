from concurrent.futures.thread import ThreadPoolExecutor
from threading import Thread
import time


def my_func(a):
    cnt = 0
    while True:
        time.sleep(1)
        print(f"Это поток {a}")
        cnt += 1
        if cnt > 3:
            break


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as e:
        e.submit(my_func, 1)
        e.submit(my_func, 1)
