def gaji(jam,duit):
    gaji = jam * duit
    print(f'Gaji mu adalah {gaji}')

while True:
    x = input("Apakah anda ingin menghitung gaji(Y/N)? ")
    if x == "Y":
        y = int(input("Berapa jam kamu bekerja : "))
        z = int(input("Berapa gajimu perjam : "))
        gaji(y,z)
    else:
        print("Jumpa di lain waktu")
        break
        
