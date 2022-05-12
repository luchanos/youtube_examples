import hashlib

from Crypto import Random
from Crypto.Cipher import AES

import os

key = os.urandom(16)  # генерируем реальный ключ (а не как в шифре Цезаря)
print("key:", key.hex())
aes = AES.new(key, AES.MODE_EAX)  # указываем способ шифрования

ciphertext, tag = aes.encrypt_and_digest(b"data")
print("Ciphertext", ciphertext.hex())

# используется для шифрования файлов


# шифрование текста
plain_text = "sample text"
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

key = hashlib.sha256(b"12345").digest()

plain_text = pad(plain_text)
iv = Random.new().read(BS)
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = (iv + cipher.encrypt(plain_text.encode()))
print("Ciphered text:", cipher_text)

# дешифровка
# iv = cipher_text[:BS]
# cipher = AES.new(key, AES.MODE_CBC, iv)
# plain_text = unpad(cipher.decrypt(cipher_text[BS:]))
# print("Plain text:", plain_text)


# обычно это не заучивают, а гуглят и смотрят бест практисез
