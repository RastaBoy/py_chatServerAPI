import hashlib

password = "live2win"


print(hashlib.algorithms_available)




print(password)
print(password.encode())


hash_obj = hashlib.sha256(password.encode())
hash_result = hash_obj.hexdigest()

print(hash_result)