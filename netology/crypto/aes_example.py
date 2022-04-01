from Crypto.Cipher import AES

import os

key = os.urandom(16)  # генерируем реальный ключ (а не как в шифре Цезаря)
print("key:", key.hex())
aes = AES.new(key, AES.MODE_EAX)  # указываем способ шифрования

ciphertext, tag = aes.encrypt_and_digest(b"data")
print("Ciphertext", ciphertext.hex())

# используется для шифрования файлов
