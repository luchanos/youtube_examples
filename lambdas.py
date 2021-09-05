def simple_func(a, b, c):
    return a + b + c


def get_el_as_sorting_key(some_tuple):
    return some_tuple[1]


# res = simple_func(1, 2, 3)
# print(res)
#
# func = lambda a, b, c: a + b + c
# print(func(1, 2, 3))


l = [(1, 2),
     (2, 100),
     (3, -8),
     (4, -10000),
     (5, -5),
     (6, 101)]

l.sort(key=get_el_as_sorting_key)
print(l)
