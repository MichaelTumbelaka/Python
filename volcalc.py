def AreaPer(Sisi):
    Area = Sisi ** 2
    print(Luas)




while True:
    Body = input("Selamat datang, apakah mau menggunakan kalkulator?(I) ")
    if Body == "I":
        Intro = (input("Area Segitiga atau Persegi?(S/P) "))
        print(f'Oke area {Intro}')
        if Intro == "S":
            def AreaSeg(Alas, Tinggi):
                Area = (Alas * Tinggi) // 2
                return(Area)
            def VolSeg(Area, TV):
                Vol = Area * TV
                print(Vol)
            x = int(input("Masukkan Alas = "))
            y = int(input("Masukkan Tinggi = "))    
            Area1 = AreaSeg(x, y)
            VolSeg(Area1, y)
            
        elif Intro == "P":
            x = int(input("Masukkan Sisi = "))
            AreaPer(x)
    else:
        break
