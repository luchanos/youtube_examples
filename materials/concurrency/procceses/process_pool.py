from multiprocessing import Pool, TimeoutError
import time
import os


def f(x):
    return x * x


if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # print same numbers in arbitrary order
        for i in pool.imap_unordered(f, range(10)):
            print(i)

        # evaluate "f(20)" asynchronously
        res = pool.apply_async(f, (20,))      # runs in *only* one process
        print(res.get(timeout=1))             # prints "400"

        # evaluate "os.getpid()" asynchronously
        res = pool.apply_async(os.getpid, ()) # runs in *only* one process
        print(res.get(timeout=1))             # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        # make a single worker sleep for 10 secs
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")



import multiprocessing as mp
import os
import time


def foo_pool(x):
    print("Sleep!")
    time.sleep(.2)
    return x*x


result_list = []
def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)


def apply_async_with_callback():
    # with mp.Pool(11) as pool:
    #     for i in range(10):
    #         res = pool.apply_async(foo_pool, args=(i, ), callback=log_result)
    #         print(res.get())
    # print(result_list)

    with mp.Pool(1) as pool:
        multiple_results = [pool.apply_async(foo_pool, args=(i, ), callback=log_result) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

    # pool = mp.Pool(11)
    # for i in range(10):
    #     pool.apply_async(foo_pool, args=(i, ), callback=log_result)
    # pool.close()
    # pool.join()
    # print(result_list)


if __name__ == '' \
               '__main__':
    apply_async_with_callback()
