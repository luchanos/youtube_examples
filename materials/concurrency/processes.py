from multiprocessing import Process
from time import sleep
from uuid import uuid4


def laborator():
    name = uuid4()
    val = 0
    for n in range(10):
        print(name, val)
        sleep(.3)
        val += 1


if __name__ == "__main__":
    process_1 = Process(target=laborator)
    process_2 = Process(target=laborator)
    process_1.start()
    # process_1.join()  # дожидаемся завершения процесса и всех дочерних процессов
    process_2.start()
