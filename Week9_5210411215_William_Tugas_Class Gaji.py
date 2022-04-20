class Gaji:
    def __init__(self,gaji_bulanan):
        self.gaji_bulanan = gaji_bulanan
    
    def total(self):
        return (self.gaji_bulanan*12)

class Pegawai:
    def __init__(self,gaji_bulanan, bonus, istri, anak):
        self.gaji_bulanan = gaji_bulanan
        self.tunjangan = istri + anak
        self.bonus = bonus
        self.obj_gaji = Gaji(self.gaji_bulanan)
        
    def hasil_tahunan(self):
        return "Total: " + str(self.obj_gaji.total() + self.bonus) + ' rupiah' + "\nTunjangan Anak dan Istri: " + str(self.tunjangan) + ' rupiah'

print("Input Data Pegawai")
gaji_input = int(input("Masukan Gaji Pegawai\t\t: "))    
bonus_input = int(input("Masukan Bonus Pegawai\t\t: "))  
tjgistri = int(input("Masukan Tunjangan Istri Pegawai\t: "))  
tjganak = int(input("Masukan Tunjangan Anak Pegawai\t: "))  
print("-"*50)
obj_pegawai = Pegawai(gaji_input,bonus_input,tjgistri,tjganak)
print(obj_pegawai.hasil_tahunan())
print("-"*50)

        