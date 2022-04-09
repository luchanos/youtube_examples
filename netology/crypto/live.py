from sys import getsizeof
import hashlib

key = hashlib.sha256(b"123").digest()
print(getsizeof(key))
print(key)
