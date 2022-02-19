# -*- coding: utf-8 -*-

# plain_text = "Секретная информация"
# key = 10
#
# alphabet = "АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя "
# ciphertext = ""
#
# for symbol in plain_text:
#     if symbol in plain_text:
#         num = alphabet.find(symbol)
#         num = num + key
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

# Дешифрация

plain_text = "ЫпфъпьчкЗИучюшъцк уЗ"
key = 10

alphabet = "АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя "
ciphertext = ""

for symbol in plain_text:
    if symbol in plain_text:
        num = alphabet.find(symbol)
        num = num - key

        if num >= len(alphabet):
            num = num - len(alphabet)

        ciphertext = ciphertext + alphabet[num]

    else:
        ciphertext = ciphertext + symbol

print(ciphertext)