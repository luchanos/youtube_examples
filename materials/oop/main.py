from abc import ABC, abstractmethod


class Ticket(ABC):
    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def to_use(self):
        pass


class AeroTicket(Ticket):
    def to_use(self):
        print("Билет на самолет использован")

    def buy(self):
        print("Билет на самолет куплен")


class BusTicket(Ticket):
    def to_use(self):
        print("Билет на автобус использован")

    def buy(self):
        print("Билет на автобус куплен")


class TicketBuyer:
    """Покупатель разных билетов"""

    menu_msg = """
Какой билет вы желаете купить?
[1] Самолет
[2] Автобус
"""
    @staticmethod
    def write_buying_data_to_db(self):
        print()

    def __call__(self, *args, **kwargs):
        ch = input(self.menu_msg)
        ticket = None
        if ch == "1":
            ticket = AeroTicket()
        elif ch == "2":
            ticket = BusTicket()
        if ticket:
            ticket.buy()


class TicketUser:
    def __call__(self, *args, **kwargs):
        print("Вы погасили билет")


class Application:
    menu_msg = """
Вас приветствует приложение luchanos!
Выберите, что желаете сделать:
[1] Купить билет
[2] Погасить билет
"""

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.ticket_buyer: TicketBuyer = None
        self.ticket_user: TicketUser = None
        self.db_clent: DbClient = None

    def run(self):
        ch = input(self.menu_msg)
        if ch == "1":
            self.ticket_buyer()
        elif ch == "2":
            self.ticket_user()


def setup_ticket_buyer(app):
    ticket_buyer = TicketBuyer()
    app.ticket_buyer = ticket_buyer
    return app


def setup_ticket_user(app):
    ticket_user = TicketUser()
    app.ticket_user = ticket_user
    return app


def setup_application_resources(app: Application):
    setup_ticket_buyer(app)
    setup_ticket_user(app)
    return app


if __name__ == "__main__":
    app = Application(__name__)
    setup_application_resources(app)
    app.run()
