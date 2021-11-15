from datetime import datetime
from multiprocessing import Process
import os

start = datetime.now()

# if os.fork() == 0:
#     padding_1 = [x for x in range(100_000_000)]
# elif os.fork() == 0:
#     padding_2 = [x for x in range(100_000_000)]


def laborator():
    print(f"{os.getpid()} Начинаю!")
    [x for x in range(100_000_000)]
    print("Закончил!")


if __name__ == "__main__":
    process_1 = Process(target=laborator)
    process_2 = Process(target=laborator)
    # process_3 = Process(target=laborator)

    process_1.start()
    process_2.start()
    # process_3.start()
    process_1.join()
    process_2.join()
    # process_3.join()

    # laborator()
    # laborator()
    # laborator()

    print(datetime.now() - start)
