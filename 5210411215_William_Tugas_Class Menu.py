#WILLIAM KESSLER SURYANTO
#PBO VII
#5210411215

class Menu :
    def __init__(self, nama, deskripsi, harga) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga

minuman1 = Menu("Jus Alpukat Ektra Milk", "Jus alpukat dengan campuran susu cokelat dan tapuran kepingan choco", 15000)
minuman2 = Menu("Jus Jambu", "Jus jambu merah tanpa gula", 8500)
minuman3 = Menu("Red & Smooth", "Smoothie pisang susu dengan strawberry", 17500)
minuman4 = Menu("Jus Alpukat", "Jus alpukat dengan gula merah", 15000)

makanan1 = Menu("Pizza", "Pizza dengan Topping Sosis", 50000)
makanan2 = Menu("Mie Ayam", "Mie Ayam dengan Pangsit", 15000)
makanan3 = Menu("Spaghetti", "Spaghetti dengan Keju", 22000)
makanan4 = Menu("Bubur", "Bubur dengan bumbu tiga rasa", 25000)

makanan = [makanan1, makanan2, makanan3, makanan4]
minuman = [minuman1, minuman2, minuman3, minuman4]

print("Daftar Menu Makanan")
for makan in makanan :
    teks = '{} harga Rp {}, {}'. format(makan.nama, makan.harga, makan.deskripsi)
    print(teks)
print("\nDaftar Menu Minuman")
for minum in minuman :
    teks = '{} harga Rp {}, {}'. format(minum.nama, minum.harga, minum.deskripsi)
    print(teks)
print("\n")