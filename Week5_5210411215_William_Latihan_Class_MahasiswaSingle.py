#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 5

#Single Inheritance
class Mahasiswa :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
#5210411215        
    def detailMhs(self) :
        return self.nim, self.nama

    def cekMhs(self) :  
        if self.nim < 150000 :
            return "Mahasiswa Aktif"
        else :
            return "Mahasiswa Tidak Terdaftar"

class Siswa(Mahasiswa) :
    def End(self) : 
        print("Mahasiswa belum melakukan daftar ulang")
#5210411215
mhs1 = Mahasiswa("Mahasiswa 1", 135103)
print(mhs1.detailMhs(), mhs1.cekMhs())
mhs2 = Siswa("Mahasiswa 2", 150503)
print(mhs2.detailMhs(), mhs2.cekMhs())
mhs2.End()

#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 5