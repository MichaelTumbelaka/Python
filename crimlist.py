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
    a = input("Masukkan Nama kriminal = ")
    b = int(input("Masukkan Umur Kriminal = "))
    c = input("Masukkan Jenis Kejahatan = ")
    d = input("Masukkan Nama kriminal = ")
    e = int(input("Masukkan Umur Kriminal = "))
    f = input("Masukkan Jenis Kejahatan = ")
    g = input("Masukkan Nama kriminal = ")
    h = int(input("Masukkan Umur Kriminal = "))
    i = input("Masukkan Jenis Kejahatan = ")
    j = input("Masukkan Nama kriminal = ")
    k = int(input("Masukkan Umur Kriminal = "))
    l = input("Masukkan Jenis Kejahatan = ")

    dic1 = {"Nama": a, "Age": b, "Crime" : c}
    dic2 = {"Nama": d, "Age": e, "Crime" : f}
    dic3 = {"Nama": g, "Age": h, "Crime" : i}
    dic4 = {"Nama": j, "Age": k, "Crime" : l}
    list1 = [dic1, dic2, dic3, dic4]   
    lengthlist1 = len(list1)
    print(f'{lengthlist1} IDENTIFIED')

    for x in list1:
            print(f'Name : {x["Nama"]}')
            print(f'Age : {x["Age"]}')
            print(f'Crime : {x["Crime"]}')
else:
    print('bla')