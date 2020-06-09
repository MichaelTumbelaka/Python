from datetime import date
hari = date.today()
tanggal = [hari.year, hari.month, hari.day]

print (hari)

year = tanggal[0]
#print (year)

while True:
    b = input("Mau menggunakan age kalk?(y/n) = ")
    if b == "y":
        x = int(input("Tanggal lahir(yyyy) = "))
        y = int(input("Tanggal lahir(mm) = "))
        z = int(input("Tanggal lahir(dd) = "))
        a = (year-1) - x 
        if tanggal[1] > y:
            print(a+1)
        elif tanggal[1] == y:
            if tanggal[2] > z:
                print(a+1)
            else:
                print(a)
        else:
            print(a)
    else:
        break


#print("Age = {z}")