import os
import asyncpg
import asyncio
from time import time
from random import randint
from uuid import uuid4


password = os.getenv('PASSWORD', None)
QUERY = """
        INSERT INTO users (username, rating)
        VALUES($1, $2);
        """


async def fill_table_users(db_pool):
    await asyncio.sleep(.1)
    await db_pool.execute(QUERY, str(uuid4()), randint(0, 1000000))


async def simple_func():
    print("Сплю")
    await asyncio.sleep(2)


async def main():
    """
    Синхронный - 19.26255202293396 - потому что всё будет идти подряд
    Асинхронный через gather - 3.5849032402038574 - потому что все будет выполняться именно асинхронно
    Асинхронный через ensure_future без await - 1.6, но вообще ничего не сделает, потому что процесс умрёт
    Асинхронный через ensure_future с await - 21, потому что дожидаемся окончания рзультата
    """
    db_pool = await asyncpg.create_pool(f"postgresql://postgres:postgres@localhost:5432/postgres")

    # for i in range(10000):
        # asyncio.ensure_future(db_pool.execute(QUERY, str(uuid4()), randint(0, 1000000)))
        # await asyncio.ensure_future(coro_or_future=fill_table_users(db_pool))
        # await fill_table_users(db_pool)

    # await simple_func()
    tasks = [db_pool.execute(QUERY, str(uuid4()), randint(0, 1000000)) for _ in range(10_000)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = time()
    asyncio.run(main())
    print(time() - start)
