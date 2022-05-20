import asyncio
from multiprocessing import Process
import os
from random import randint
import time


def laborator():
    result = 0
    time.sleep(10)
    print(os.getpid(), result)


async def sleeper():
    # await asyncio.sleep(10)
    # print("I slept")
    p = Process(target=laborator)
    p.start()


async def main():
    tasks = [sleeper() for _ in range(10)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
