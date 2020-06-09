class Flower:
    def __init__(self, name, petal, price):
        self.name = name
        self.petal = petal
        self.price = price
        print(f'Nama bunga = {self.name}')
        print(f'Jumlah petal = {self.petal}')
        print(f'Harga per piece = Rp {self.price}')
    def vary(self):
        harga = (self.petal) * (self.price)
        print (f'Harga total = Rp {harga}')
x = input("Nama bunga = ")
y = int(input("Jumlah petal = "))
z = float(input("Harga satuan = "))
bunga = Flower(x, y, z)
bunga.vary()