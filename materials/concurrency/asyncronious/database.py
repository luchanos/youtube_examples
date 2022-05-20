import os
import asyncpg
import asyncio
from time import time


password = os.getenv('PASSWORD', None)
QUERY = """
        INSERT INTO users 
        VALUES($1, $2, $3);
        """


async def fill_table_users(db_pool):
    await db_pool.execute(QUERY, 'username', 'lastname', 18)


async def simple_func():
    print("Сплю")
    await asyncio.sleep(10)


async def main():
    """
    Синхронный - 19.26255202293396
    Асинхронный через gather - 3.5849032402038574
    Асинхронный через ensure_future - 19
    """
    db_pool = await asyncpg.create_pool(f"postgresql://postgres:postgres@localhost:5432/postgres")

    for i in range(10000):
        # asyncio.ensure_future(coro_or_future=fill_table_users(db_pool))
        await fill_table_users(db_pool)
    # await simple_func()
    # await asyncio.gather(*[asyncio.create_task(fill_table_users(db_pool)) for _ in range(10_000)])


if __name__ == "__main__":
    start = time()
    asyncio.run(main())
    print(time() - start)
