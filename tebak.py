import random

y = random.randint(1, 10)
print(y)
x = int(input("Berapakah Umur adik saya? "))
while x != y:
    if x > y:
        x = int(input("kebesaran, coba lagi"))
    if x < y:
        x= int(input("kekecilan, coba lagi"))
    if x == y:
        print("kamu berhasil")


        



        