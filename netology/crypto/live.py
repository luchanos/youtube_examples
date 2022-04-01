# вспомним строки:
s = "123"
s1 = "a"  # тоже строка

print(chr(119))
print(ord("w"))

# строки можно складывать и умножать на число
print("a" * 10)
print("a" + "b" + "c")

"\n"  # экранирование переноса строки

# строки поддерживают срезы
s = "0123456789"
print(s[1:5])


# Запись строки наоборот:
plain_text = "Очень секретная информация"  # начальный текст
ciphertext = ""  # зашифрованный текст

i = len(plain_text) - 1

while i >= 0:
    ciphertext = ciphertext + plain_text[i]
    i = i - 1

print(ciphertext)
