#WILLIAM KESSLER SURYANTO
#PBO VII
#5210411215

class Mahasiswa :
    def __init__ (self, nama, nim, prodi) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

mahasiswa1 = Mahasiswa("William", "5210411215", "Informatika")
mahasiswa2 = Mahasiswa("Dicka", "5210411229", "Informatika")
mahasiswa3 = Mahasiswa("Havin", "5210411212", "Informatika")
mahasiswa4 = Mahasiswa("Rifqi", "5210411211", "Informatika")

mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("List Mahasiswa Informatika")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {}'. format(mhs.nama, mhs.prodi, mhs.nim )
    print(teks)
print("\n")
