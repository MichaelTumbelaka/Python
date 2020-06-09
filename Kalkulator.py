while True:
    Intro = input("Apakah anda ingin menggunakan kalkulator?(Y/N) : ")
    if Intro == "Y":
        print("==========")
        print("Calculator")
        print("==========")
        Angka1 = int(input("Masukkan angka pertama : "))
        print(f'Angka pertamamu adalah {Angka1}')
        print("1 = tambah")
        print("2 = kurang")
        print("3 = kali")
        print("4 = bagi")
        Operasi = input('Masukkan operasi bilangan : ')
        if Operasi == "1":
            print(f"Angka operasimu adalah {Operasi}")
            Angka2 = (int(input("Masukan angka kedua : ")))
            print(f"Angka keduamu adalah {Angka2}")
            Hasil = (Angka1 + Angka2)
            print(f'Hasil : {Hasil}')
        elif Operasi == "2":
            print(f"Angka operasimu adalah {Operasi}")
            Angka2 = (int(input("Masukan angka kedua : ")))
            print(f"Angka keduamu adalah {Angka2}")
            Hasil = (Angka1 - Angka2)
            print(f'Hasil : {Hasil}')
        elif Operasi == "3":
            print(f"Angka operasimu adalah {Operasi}")
            Angka2 = (int(input("Masukan angka kedua : ")))
            print(f"Angka keduamu adalah {Angka2}")
            Hasil = (Angka1 * Angka2)
            print(f'Hasil : {Hasil}')
        elif Operasi == "4":
            print(f"Angka operasimu adalah {Operasi}")
            Angka2 = (int(input("Masukan angka kedua : ")))
            print(f"Angka keduamu adalah {Angka2}")
            Hasil = (Angka1 // Angka2)
            print(f'Hasil : {Hasil}')
    else:
        break
