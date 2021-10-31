class CustomClass:
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __str__(self):
        return f"Это вывод информации из метода __str__:" \
               f"\nПоле 1: {self.field_1}" \
               f"\nПоле 2: {self.field_2}"

    def __repr__(self):
        return f"Это вывод информации из метода __repr__:" \
               f"\nПоле 1: {self.field_1}" \
               f"\nПоле 2: {self.field_2}"


obj_1 = CustomClass(1, 2)
obj_2 = CustomClass(3, 4)
# print(obj_1)
# print(obj_2)

# если есть метод __repr__, то вывод информация будет выводиться посредство использования
# метода __repr__. В противном случае будет использован вывод по умолчанию.
c = [obj_1, obj_2]
print(c)
