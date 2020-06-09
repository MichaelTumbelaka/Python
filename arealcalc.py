def AreaSeg(Alas, Tinggi):
    Area = (Alas * Tinggi) // 2
    print(Area)
def AreaPer(Sisi):
    Area = Sisi ** 2
    print(Area)

while True:
    Body = input("Selamat datang, apakah mau menggunakan kalkulator?(I) ")
    if Body == "I":
        Intro = (input("Area Segitiga atau Persegi?(S/P) "))
        print(f'Oke area {Intro}')
        if Intro == "S":
            x = int(input("Masukkan Alas = "))
            y = int(input("Masukkan Tinggi = "))    
            AreaSeg(x, y)
        elif Intro == "P":
            x = int(input("Masukkan Sisi = "))
            AreaPer(x)
    else:
        break

