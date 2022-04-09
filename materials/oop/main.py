"""
История одного бизнеса:

мы решили открыть лавочку, которая авторизована для того, чтобы продавать билеты на автобус. Есть БД
в которую пишут все.

что означает продать билет? это значит совершить определенный набор действий:
    - осуществить запись в базу
    - осуществить отправку электронного билета на почту
    - осуществить отправку смс на телефон
"""


class Application:
    def __init__(self, name):
        self.name = name


class Ticket:
    def send_ticket_to_email(self):
        print("Отправляю на почту билет")

    def send_sms(self):
        print("Отправляю смс")

    def __call__(self, *args, **kwargs):
        self.send_ticket_to_email()
        self.send_sms()


class BusTicketSeller(Ticket):
    def write_to_db(self):
        print("Пишу в базу")

    def __call__(self, *args, **kwargs):
        self.write_to_db()
        super().__call__(*args, **kwargs)


class AviaTicketSeller(Ticket):
    def send_data_to_aviacompany(self):
        print("Отправляю данные в авиакомпанию")

    def validate_passport(self):
        print("Валидирую паспорт")

    def __call__(self, *args, **kwargs):
        self.validate_passport()
        self.send_data_to_aviacompany()
        super().__call__(*args, **kwargs)


class TicketRouter:
    MAPPER = {
        "avia": AviaTicketSeller,
        "bus": BusTicketSeller
    }

    def __call__(self, *args, **kwargs):
        ch = input("Введите bus или avia: ")
        ticket_buyer = self.MAPPER[ch]()
        ticket_buyer()


if __name__ == "__main__":
    app = Application("my_shiny_application")

    ticket_router = TicketRouter()
    app.ticket_seller = ticket_router
    app.ticket_seller()
