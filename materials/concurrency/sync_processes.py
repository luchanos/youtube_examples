from multiprocessing import Process
from datetime import datetime
import time


def sleeper():
    time.sleep(4)


if __name__ == "__main__":
    start = datetime.now()
    p = Process(target=sleeper)
    p.start()
    print("Main process has been finished! Execution time: ", datetime.now() - start)
