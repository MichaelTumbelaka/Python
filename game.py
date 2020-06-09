import random

y = random.randint(1, 10)
print(y)
x = int(input("Berapakah Umur adik saya? "))
if  x != y:
    while x < y:
        input("kekecilan, coba lagi ")
    while x > y:
        input("kebesaran, coba lagi ")
else:
    print("Kamu berhasil")