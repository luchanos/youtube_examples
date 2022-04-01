# КОД НА СТОРОНЕ КЛИЕНТА
import socket
from datetime import datetime
from time import sleep
import sys

from logging import getLogger, StreamHandler


# просто удобное логирование
logger = getLogger(__name__)
stdout_handler = StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)
logger.setLevel("DEBUG")

# sock = socket.socket()
# sock.connect(("127.0.0.1", 10002))  # заблокируется до тех пор, пока сервер на своей стороне

# или
sock = socket.create_connection(("127.0.0.1", 10002), timeout=5)  # таймаут на установку соединения
sock.settimeout(2)  # таймаут на работу с сокетом


# не вызовет accept
# sock.sendall("ping".encode("utf-8"))
with sock:
    while True:
        data_for_sending = str(datetime.now()).encode("utf-8")
        sock.sendall(data_for_sending)
        logger.info(f"I am send that data: {data_for_sending}")
        sleep(1)

# более короткая запись
# sock.sendall("ping".encode("utf-8"))
# sock.close()

# А теперь можно разнести код по разным файлам и посмотреть, как один код будет
# отправлять запросы, а другой их принимать
