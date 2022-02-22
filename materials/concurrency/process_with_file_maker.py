import time
from random import randint
import os
from datetime import datetime
from multiprocessing import Process

# with open("file.txt", "w") as f_o:
#     for _ in range(100_000_00):
#         f_o.write(f"{randint(0, 9)}\n")


def laborator():
    result = 0
    with open("file.txt", "r") as f_o:
        for s in f_o:
            # pass
            result += randint(0, int(s))  # именно на эту строчку будут приходиться основные расходы
    print(os.getpid(), result)


# if __name__ == "__main__":
#     # пул процессов удобен для того, чтобы одну и ту же функцию вызвать
#     # в нескольких потоках с разными аргументами
#     with multiprocessing.Pool(4) as pool:
#         pool.map(laborator, (1, 2, 3))


# простой синхронный запуск - 0:00:20.334723
# if __name__ == "__main__":
#     start = datetime.now()
#     laborator()
#     laborator()
#     print(datetime.now() - start)


# запуск с процессами - 0:00:09.633758
# if __name__ == "__main__":
#     start = datetime.now()
#     p = Process(target=laborator)
#     p_1 = Process(target=laborator)
#     p.start()
#     p_1.start()
#     p.join()  # не пойдём дальше до тех пор, пока p не завершится
#     print("p завершился")
#     p_1.join()  # не пойдём дальше до тех пор, пока p_1 не завершится
#     print("p_1 завершился")
#     print(datetime.now() - start)


# запуск с процессами + рефакторинговый лайфхак - 0:00:15.565276
if __name__ == "__main__":
    start = datetime.now()
    p_list = [Process(target=laborator) for _ in range(2)]
    for p in p_list:
        p.start()
    for p in p_list:  # без этого основной поток завершит работу, но это не помешает работать дочерним
        p.join()
    print(datetime.now() - start)
