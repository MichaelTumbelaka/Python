import time

password = input("Password? ")
if password == "1234":
    print("--------------------")
    print("FBI MOST WANTED LIST")
    print("--------------------")
    for x in range(0,3):
        for x in range(0,4):
            print(f'Loading Data{"." * x}')
            time.sleep(0.5)
    kumpulan = []
    kriminal = {}

    def mt(kumpulan)
        for kumpulan in kriminals:
            for val, key in kumpulan.items():
                print(key, value)
    
    def dalem():
        nama = input("Name of the criminal? ")
        umur = input("Age of the criminal? ")
        crime = input("Crime of the criminal? ")
        return nama, umur, crime

    while True:
        nama, umur, crime = bio()
        kriminal["nama"] = nama
        kriminal["umur"] = umur
        kriminal["crime"] = crime

        kumpulan.append(kriminal)

        lagi = input("Masukkan lagi? ")
        if lagi == "y":
            continue
        else:
            break
mt(kumpulan)




