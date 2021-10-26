from uuid import uuid4


class Tumbochka:
    tumb_cnt = 0

    def __init__(self):
        self.tumb_id = uuid4()
        Tumbochka.tumb_cnt += 1

    def open_box(self):
        print(f"Ящик тумбочки с id {self.tumb_id} открыт")

    @staticmethod
    def cut_by_scissors(smth):
        print(f"Достали ножницы и режем {smth}")

    @classmethod
    def show_me_total_tumb_count(cls):
        return cls.tumb_cnt


class TechOrder:
    GET_ORDER_BY_ID = """SELECT * FROM tech_orders WHERE order_id = $1"""
    ORDER_STATUSES_MAPPER = {
        0: "open",
        1: "need info",
        2: "in progress",
        3: "solved"
    }

    def __init__(self, description, severity, status, order_id=None):
        self.order_id = order_id or uuid4()
        self.description = description
        self.severity = severity
        self.status = status

    def check_status(self):
        return self.ORDER_STATUSES_MAPPER[self.status]

    @classmethod
    def get_order_by_id(cls, order_id):
        print(f"Делаю запрос в базу: {cls.GET_ORDER_BY_ID}")
        # нам что-то вернётся из базы:
        res = {
            "order_id": order_id,
            "description": f"описание технической заявки {order_id} из БД",
            "severity": f"степень приоритетности заявки {order_id} из БД",
            "status": f"статус заявки {order_id} из БД"
        }
        return TechOrder(**res)

    def __str__(self):
        return f"Заявка: {self.order_id}\n" \
               f"Описание: {self.description}\n" \
               f"Приоритетность: {self.severity}\n" \
               f"Статус: {self.status}\n"


order = TechOrder.get_order_by_id(123)
print(order)
