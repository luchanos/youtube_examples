# from sys import getsizeof
# import hashlib
#
# key = hashlib.sha256(b"123").digest()
# print(getsizeof(key))
# print(key)
#
#
# def summarizer(arg1, arg2):
#     return arg1 + arg2
#
#
# x = lambda arg1, arg2: arg1 + arg2
# print(x(1, 2))


import time


def cashe_with_timer(sec):
    def cashe(func):
        cash_dict = {}
        start = time.perf_counter()

        def wrapper(*args, **kwargs):
            if cash_dict.get('time', 0) > sec:
                cash_dict.clear()
            else:
                finish = time.perf_counter()
                cash_dict['time'] = finish - start
            return cash_dict.setdefault(args, func(*args, **kwargs)) if args not in cash_dict else cash_dict[args]

        return wrapper
    return cashe


@cashe_with_timer(100)
def division(a, b):
    time.sleep(1)
    return a / b


print(division(1, 2))
print(division(1, 2))
print(division(1, 2))
print(division(1, 2))
print(division(1, 2))
print(division(1, 4))
print(division(1, 2))
print(division(1, 4))
print(division(1, 3))
