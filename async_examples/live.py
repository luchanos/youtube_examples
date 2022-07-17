import asyncio
import random
from time import sleep, time
import uuid


async def sleeper():
    c_id = uuid.uuid4()
    sleep_time = random.randint(0, 1)
    print(f"Я {c_id} сплю {sleep_time} секунд!")
    await asyncio.sleep(sleep_time)
    print(c_id, "спать закончила!")
    return c_id


async def main_function():
    """Основная точка входа для работы нашего скрипта или приложения"""
    res = await asyncio.gather(sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(),
                               sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(),
                               sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(),
                               sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(),
                               sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(),
                               sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper(), sleeper()
                               )
    print(res)

start = time()
asyncio.run(main_function())
print(time() - start)
