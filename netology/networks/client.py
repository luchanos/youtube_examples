# КОД НА СТОРОНЕ КЛИЕНТА
import socket
from datetime import datetime
from time import sleep


# заблокируется до тех пор, пока сервер на своей стороне
sock = socket.create_connection(("127.0.0.1", 10002), timeout=5)  # таймаут на установку соединения
sock.settimeout(2)  # таймаут на работу с сокетом

# не вызовет accept
with sock:
    while True:
        data_for_sending = str(datetime.now()).encode("utf-8")
        sock.sendall(data_for_sending)
        print(f"I am send that data: {data_for_sending}")
        sleep(1)

# А теперь можно разнести код по разным файлам и посмотреть, как один код будет
# отправлять запросы, а другой их принимать
