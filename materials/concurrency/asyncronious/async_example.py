import asyncio


async def simple_func():
    print("Сплю")
    await asyncio.sleep(1)


async def main():
    for _ in range(100):
        asyncio.ensure_future(coro_or_future=simple_func())


asyncio.run(main())
