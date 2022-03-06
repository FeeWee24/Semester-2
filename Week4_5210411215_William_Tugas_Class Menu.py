#WILLIAM KESSLER SURYANTO
#PBO VII
#5210411215

class Menu :
    def __init__(self, nama, deskripsi, harga, menu_pelengkap, harga_tambahan) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__menu_pelengkap = menu_pelengkap
        self.__harga_tambahan = harga_tambahan

minuman1 = Menu("Jus Alpukat Ektra Milk", "Jus alpukat dengan campuran susu cokelat dan tapuran kepingan choco", 15000, "Es Krim Vanilla", 3000)
minuman2 = Menu("Jus Jambu", "Jus jambu merah tanpa gula", 8500, "Es Krim Cokelat", 3000)
minuman3 = Menu("Red & Smooth", "Smoothie pisang susu dengan strawberry", 17500, "Oreo Bubuk", 2000)
minuman4 = Menu("Jus Alpukat", "Jus alpukat dengan gula merah", 15000, "Susu Kental Manis", 4000)

makanan1 = Menu("Pizza", "Pizza dengan Topping Sosis", 50000, "Mozarella", 15000)
makanan2 = Menu("Mie Ayam", "Mie Ayam dengan Pangsit", 15000, "Bakso", 5000)
makanan3 = Menu("Spaghetti", "Spaghetti dengan Keju", 22000, "Sosis dan Kornet", 8000)
makanan4 = Menu("Bubur", "Bubur dengan bumbu tiga rasa", 25000, "Kacang dan Sate Usus", 3000)

makanan = [makanan1, makanan2, makanan3, makanan4]
minuman = [minuman1, minuman2, minuman3, minuman4]

print("Daftar Menu Makanan")
for makan in makanan :
    teks = '{} harga Rp {}, {}. Dengan menambah Rp {} anda bisa mendapatkan Extra {}.'. format(makan.nama, makan.harga, makan.deskripsi, makan._Menu__harga_tambahan, makan._Menu__menu_pelengkap)
    print(teks)
print("\nDaftar Menu Minuman")
for minum in minuman :
    teks = '{} harga Rp {}, {}. Dengan menambah Rp {} anda bisa mendapatkan Topping tambahan {}.'. format(minum.nama, minum.harga, minum.deskripsi, minum._Menu__harga_tambahan, minum._Menu__menu_pelengkap)
    print(teks)
print("\n")
