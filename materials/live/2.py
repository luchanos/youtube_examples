def deco(func):
    """Это объемлющая коробка"""
    def inner(*args, **kwargs):
        """Пустое пространство для чего угодно"""
        print("Покупайте наших котиков!")
        return func(*args, **kwargs)
    return inner


def summarize(a, b):
    return a + b


@deco
def fff():
    return 1


print(fff())
summarize_decorized = deco(summarize)
# print(summarize(1, 2))
# print(summarize(1, 2))
# print(summarize(1, 2))
# print(summarize(1, 2))
# print(summarize(1, 2))
# print(summarize(1, 2))
# print(summarize(1, 2))
# print(summarize(1, 2))
