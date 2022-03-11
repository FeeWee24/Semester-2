#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 5

class ComputerPart:
    def __init__(self, pabrikan, nama, jenis, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.jenis = jenis
        self.harga = harga

class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed) :
        super().__init__(pabrikan, nama, 'processor', harga)
        self.jumlah_core = jumlah_core
        self.speed = speed
#5210411215
class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas) :
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas = kapasitas 
    
class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm) :
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm  
#5210411215
p = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz')
m = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)

parts = [p, m, hdd]
for part in parts :
    print('{} {} produksi {}'.format(part.jenis, part.nama, part.pabrikan))
    
#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 5