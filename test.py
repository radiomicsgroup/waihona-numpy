from waihonanumpy import RedisStorage
import numpy as np

r = RedisStorage("password", testing=True)

i = np.identity(3)
a = np.arange(15).reshape(3, 5)
a2= a*2
ii = np.arange(21).reshape(3, 7)

r["p1","r1"] = a

a_prime_key, a_prime_value = r["p1","r1"] 

if (a == a_prime_value).all():
    print("ok !")
else:
    print("Error")

r["p1","r2"] = a2 
r["p2","r100"] = i

resultA = r["p1","*"]
print(resultA)

resultB = r["p*","*"]
print(resultB)

r["p1","*"] = ii
resultZ = r["p1","*"] 
print(resultZ)

del r["p1","*"]
resultBZ = r["p*","*"]
print(resultBZ)