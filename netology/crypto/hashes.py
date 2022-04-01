import hashlib

text = "Секретная информация"  # .split()

# с помощью md5 (устаревшее)
for i in text:
    md5 = hashlib.md5(i.encode())

    print(i, ":", md5.hexdigest())  # размер хэша всегда будет одинаковым

# неустойчив, ломается радужными таблицами. поэтому придумали "солить"

# с помощью SHA256 / SHA512
# dk = hashlib.pbkdf2_hmac('sha256', text.encode(), b'salt', 100000)  # алгоритм, данные, соль, длинна ключа
# print(dk.hex())
