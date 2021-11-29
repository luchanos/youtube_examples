class Vector:
    """класс описывающий обычный 2D-вектор"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """сложение вектора с вектором"""
        new_x = self.x + other.x
        new_y = self.y + other.y
        result_object = Vector(new_x, new_y)
        return result_object

    def __sub__(self, other):
        """вычитание из вектора вектор"""
        new_x = self.x - other.x
        new_y = self.y - other.y
        result_object = Vector(new_x, new_y)
        return result_object

    def __mul__(self, other):
        """умножение на число"""
        new_x = self.x * other
        new_y = self.y * other
        result_object = Vector(new_x, new_y)
        return result_object

    def __mod__(self, other):
        """остаток от деления на число"""
        new_x = self.x % other
        new_y = self.y % other
        result_object = Vector(new_x, new_y)
        return result_object

    def __truediv__(self, other):
        """обычное деление на число"""
        new_x = self.x / other
        new_y = self.y / other
        result_object = Vector(new_x, new_y)
        return result_object

    def __floordiv__(self, other):
        """целочисленное деление на число"""
        new_x = self.x // other
        new_y = self.y // other
        result_object = Vector(new_x, new_y)
        return result_object

    def __str__(self):
        """метод для вывода информации об объекте"""
        return f"x: {self.x}, y: {self.y}"


ex_1 = Vector(1, 2)
ex_2 = Vector(3, 4)
print(ex_1 % 2)

print(ex_1 + ex_2 + ex_2)
