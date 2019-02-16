# mencari nilai n bilangan acak < 0.5 dengan fungsi random
print()
print("=================================================")
print("Program menampilkan bilangan acak kurang dari 0.5")
print("=================================================")
print()

import random

print ("bilangan random antara 0 <= n < 0.5 :")
random.random()

import random

n = int(input("Masukan nilai N : "))
for i in range(n) :
    a=random.uniform(0.0,0.5)
    print ("Data ke : ", i, "=> ", a)
