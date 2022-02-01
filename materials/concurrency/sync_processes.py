from multiprocessing import Process
from datetime import datetime
import time
import os


def sleeper():
    time.sleep(40)
    print(f"Process with PID {os.getpid()} has been finished!")


# os.fork()
# time.sleep(10)

if __name__ == "__main__":
    start = datetime.now()
    p = Process(target=sleeper)
    p.start()
    time.sleep(10)
    print(f"Main process with PID {os.getpid()} has been finished! Total execution time: ", datetime.now() - start)
