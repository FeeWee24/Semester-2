#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 6

class ComputerPart:
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama    
        self.harga = harga
#5210411215
class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, core, speed) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        self.core = core
        self.speed = speed
        
    def Tampil(self) :  
        print(f"{self.pabrikan} membuat seri produk yaitu {self.nama}")
        print("Dengan Spesifikasi Berikut:")
        print(f"Jumlah Core = {self.core}")
        print(f"Boost Clock: {self.speed}")
        print(f"Harga : {harga_brg(self.harga)}")
#5210411215
class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga

    def Tampil(self, kapasitas) :  
        print(f"{self.pabrikan} membuat seri produk yaitu {self.nama}")
        print("Dengan Spesifikasi Berikut:")
        print(f"Kapasitas : {kapasitas}")
        print(f"Harga : {harga_brg(self.harga)}")
#5210411215
class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
    
    def Tampil(self, kapasitas, rpm) :
        print(f"{self.pabrikan} membuat seri produk yaitu {self.nama}")
        print("Dengan Spesifikasi Berikut:")
        print(f"Kapasitas : {kapasitas}")
        print(f"RPM : {rpm}")
        print(f"Harga : {harga_brg(self.harga)}")
#5210411215        
class GraphicsCard(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, MHz) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        self.MHz = MHz
    
    def Tampil(self, kapasitas) :
        print(f"{self.pabrikan} membuat seri produk yaitu {self.nama}")
        print("Dengan Spesifikasi Berikut:")
        print(f"Kapasitas : {kapasitas}")
        print(f"MHz : {self.MHz}")
        print(f"Harga : {harga_brg(self.harga)}")

def harga_brg(harga) :
    x = str(harga)
    if len(x) <= 3 :
        return "Rp." + x
    else :  
        a = x[:-3]
        b = x[-3:]
        return harga_brg(a) + '.' + b
        
#5210411215
proci = Processor('AMD', 'Ryzen™ 7 5800X', 6500000, 8, '4.7GHz')
ram = RandomAccessMemory('Corsair', 'Corsair Vengeance DDR4 Dimm PC4-28800/3600MHz', 1500000)
hdd = HardDiskSATA('WD Black', 'WD Black Caviar Dekstop HDD 3.5 inch', 2100000)
vga = GraphicsCard('NVIDIA', 'NVIDIA RTX 3080 TI', 35000000, 1670)

parts = [proci, ram, hdd, vga]   
print("\n\t\t\t\tPart Komputer Overloading")
print("---------------------------------------------------------------------------------\n")
proci.Tampil()
ram.Tampil("2x8GB")
hdd.Tampil("1TB", 7200)
vga.Tampil("12GB")
print("---------------------------------------------------------------------------------")

#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 6