# просто класс Матрёшки - по сути это чертеж матрёшки, в котором сказано чем должна обладать каждая из них и что уметь
class Matryoshka:
    def __init__(self, dress_color, eye_color, name):
        print(f"Запускается метод __init__ и наделяет экземпляр типа {self.__class__} переданными характеристиками")
        self.dress_color = dress_color
        self.eye_color = eye_color
        self.name = name

    def __new__(cls, *args, **kwargs):
        print(f"Запускается метод __new__ и аллоцирует память для хранения экземпляра типа {cls}")
        return super().__new__(cls)

    def say_hello(self):
        print(f"Hello, <username> from {self.name}!")

    def __str__(self):
        return f"Matryoshka {self.name}"


# собираем экземпляр класса Матрёшки
print(Matryoshka)
c = Matryoshka("Red", "Blue", "Kate")
print(c)
