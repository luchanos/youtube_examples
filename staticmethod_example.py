from uuid import uuid4


class Tumbochka:
    def __init__(self):
        self.tumb_id = uuid4()

    def open_box(self):
        print(f"Ящик тумбочки с id {self.tumb_id} открыт")

    @staticmethod
    def cut_by_scissors(smth):
        print(f"Достали ножницы и режем {smth}")


tumbochka = Tumbochka()
tumbochka.open_box()
tumbochka.cut_by_scissors("paper")
Tumbochka.cut_by_scissors("paper")
