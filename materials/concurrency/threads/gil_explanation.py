# import dis
#
#
# def sum_2(a, b):
#     с = 1
#     raise Exception
#     return a + b
#
#
# dis.dis(sum_2)


# import threading
#
# a = 0
#
#
# def x():
#     global a
#     for i in range(100000):
#         a += 1
#
#
# threads = []
#
# for j in range(2):
#     thread = threading.Thread(target=x)
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# assert a == 200000


#### LOCK

# from threading import Lock
#
# import threading
#
# a = 0
# lock = Lock()
#
#
# def x():
#     global a
#     lock.acquire()
#     for i in range(100000):
#         a += 1
#     lock.release()
#
#
# threads = []
#
# for j in range(2):
#     thread = threading.Thread(target=x)
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print(a)
# assert a == 200000
