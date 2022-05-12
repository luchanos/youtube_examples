import asyncio
from asyncio import sleep
from uuid import uuid4


async def my_func():
    name = uuid4()
    for n in range(10):
        print(f"Работаем из {name}")
        await sleep(1)


async def main():
    tasks = [my_func() for _ in range(100)]
    await asyncio.gather(*tasks)


asyncio.run(main())
