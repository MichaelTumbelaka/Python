class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        print(f'Alas = {self.alas}')
        print(f'Tinggi = {self.tinggi}')
    def volume(self, ting):
        volume = ((self.alas * self.tinggi)//2) * ting
        print (f'Volume = {volume}')
x = int(input("Masukkan alas segitiga = "))
y = int(input("Masukkan tinggi segitiga = "))
z = int(input("Masukkan tinggi volume = "))
segitiga = Segitiga(x,y)
segitiga.volume(z)