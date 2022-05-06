# КОД НА СТОРОНЕ СЕРВЕРА
import socket
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # семейство сокета (Internet протоколы) и его тип (потоковый)
# подробная информация содержится в оф. документации
sock.bind(("127.0.0.1", 10002))  # max port 65335
sock.listen(socket.SOMAXCONN)  # слушаем хост и порт и задаём макс. количество входящих соединений

conn, addr = sock.accept()  # начинаем принимать входящее клиентское соединение
# бесконечно читаем из нашего соединния
conn.settimeout(500)  # таймаут в секундах для ожидания сервера, что подсоединившийся клиент что-то даст
# 0 - неблокирующий режим. None - это бесконечное ожидание, что данные прочитают
with conn, sock:
    while True:
        time.sleep(1)
        received_data = conn.recv(1024)
        # обратите внимание, что данные прилетают в виде байтов!
        print(f"I am received that data: {received_data}")
        # print(received_data.decode("utf-8"))

# если юзаем менеджер контекста, то не нужно
# conn.close()
# sock.close()
