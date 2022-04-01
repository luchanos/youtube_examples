# -*- coding: utf-8 -*-

plain_text = "Секретная информация"
key = 10  # это наш закрытый ключ, который надо передавать по защищенному каналу

alphabet = "АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя "
ciphertext = ""

for symbol in plain_text:
    if symbol in alphabet:  # только если символ есть в нашем алфавите. если нету - не шифруем
        num = alphabet.find(symbol)
        num = num + key

        if num >= len(alphabet):
            num = num - len(alphabet)

        ciphertext = ciphertext + alphabet[num]

    else:
        ciphertext = ciphertext + symbol

print(ciphertext)


# Дешифрация

# plain_text = "ЫпфъпьчкЗИучюшъцк уЗ"
# key = 10
#
# alphabet = "АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя "
# ciphertext = ""
#
# for symbol in plain_text:
#     if symbol in alphabet:
#         num = alphabet.find(symbol)
#         num = num - key
#
#         if num >= len(alphabet):
#             num = num - len(alphabet)
#
#         ciphertext = ciphertext + alphabet[num]
#
#     else:
#         ciphertext = ciphertext + symbol
#
# print(ciphertext)

# ВОПРОС! Как взломть этот алгоритм?


# как вариант использовать запутанный алфавит, но и его можно хакнуть
