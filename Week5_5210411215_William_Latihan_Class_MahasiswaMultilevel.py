#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 5

#Multilevel Inheritance
class Mahasiswa() :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
#5210411215
class Siswa1(Mahasiswa) :
    def __init__(self, nama, nim):
        super().__init__(nama, nim)
        
class Siswa2(Siswa1) :
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim  
#5210411215
mahasiswa1 = Mahasiswa("Mikasa", 135105)
mahasiswa2 = Siswa1("Nezuko", 135117)
mahasiswa3 = Siswa2("Hancock", 134079)

print(mahasiswa1.nama, mahasiswa1.nim)
print(mahasiswa2.nim)   
print(mahasiswa3.nama)

#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 5