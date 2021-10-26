def notification_by_email():
    print("Оповещаю пользователя о событии по смс")


def notification_by_sms():
    print("Оповещаю пользователя о событии по смс")


class MyNotifierClass:
    def __init__(self, token, some_other_data):
        self.token = token
        self.some_other_data = some_other_data

    def some_actions_due_to_notification(self):
        print(f"Какие-то побочные действия с объектом {self} во время нотификаций")

    def __call__(self, *args, **kwargs):
        print("Оповещение чего-то куда-то из экземпляра класса")


notification_methods = [notification_by_email, notification_by_sms, MyNotifierClass(123123, 123123)]

for notification in notification_methods:
    notification()
