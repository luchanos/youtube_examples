from functools import partial


def make_request(a, b, c):
    print("Делаю запрос с параметрами", a, b, c)


def write_to_db(a, b):
    print("Пишу в базу информацию", a, b)


def calculate_smth(a, b, c, d, e):
    print("Обсчитываю значения", a, b, c, d, e)


mapper = {
    "1": partial(make_request, 1, 2, 3),
    "2": partial(write_to_db, 1, 2),
    "3": partial(calculate_smth, 1, 2, 3, 4, 5)
}


class Partial:
    def __init__(self, func, *args, **kwargs):
        self.to_be_executed = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        return self.to_be_executed(*self.args, **self.kwargs)


mapper = {
    "1": Partial(make_request, 1, 2, 3),
    "2": Partial(write_to_db, 1, 2),
    "3": Partial(calculate_smth, 1, 2, 3, 4, 5)
}


res = input("Выберите опцию ")
mapper[res]()
