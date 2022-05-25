from threading import Thread, Lock
import time

lock = Lock()


# def my_func():
#     cnt = 0
#     lock.acquire()
#     for _ in range(50_000_000):
#         cnt += 1
#     lock.release()


# def my_sleepy_func():
#     time.sleep(2)


# синхронно - 4.6с - потому что мы не создаём потоки и кучу всякой обвязки для них
# 2 потока - 5.2с - дольше, потому что испытываем накладные расходы на переключение контекста между потоками
# 2 потока с запросом блокировки - 4.7с - почти как и в синхронном случае, потому что уменьшаем накладные расходы
# на переключение

def io_example():
    data = input("Введите какие-то данные: ")


def sleeper_cycler():
    cnt = 0
    while cnt < 100_000_000:
        if cnt % 10_000_000 == 0:
            # print(cnt)
            pass
        cnt += 1


th_1 = Thread(target=sleeper_cycler)
th_2 = Thread(target=io_example)
th_1.start()
th_2.start()
th_2.join()
th_1.join()

start = time.time()
# t = Thread(target=my_func)
# t_1 = Thread(target=my_func)
# t.start()
# t_1.start()
# t.join()
# t_1.join()
# my_func()
# my_func()

# t_1 = Thread(target=my_sleepy_func)
# t_2 = Thread(target=my_sleepy_func)
# t_1.start()
# t_2.start()
# t_2.join()
# t_1.join()
print("Время работы программы:", time.time() - start)
