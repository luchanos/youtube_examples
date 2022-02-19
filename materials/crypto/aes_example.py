from Crypto.Cipher import AES

import os

key = os.urandom(16)
print("key:", key.hex())
aes = AES.new(key, AES.MODE_EAX)

ciphertext, tag = aes.encrypt_and_digest(b"data")
print("Ciphertext", ciphertext.hex())

# закончил на 51 минуте