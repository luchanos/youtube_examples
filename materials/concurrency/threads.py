from threading import Thread
from uuid import uuid4
from time import sleep
from concurrent.futures import ThreadPoolExecutor


def laborator():
    name = uuid4()
    val = 0
    for n in range(10):
        print(name, val)
        sleep(1)
        val += 1


# thread_1 = Thread(target=laborator)
# thread_2 = Thread(target=laborator)
# thread_1.run()
# thread_2.run()
pool = ThreadPoolExecutor(max_workers=10)
with pool:
    results = [pool.submit(laborator) for i in range(100)]
