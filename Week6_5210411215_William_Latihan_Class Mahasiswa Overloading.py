#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 6

#Implementasi Overloading Class Mahasiswa
class Mahasiswa :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
    
    def tampilMhs(self) :
        print(f"Nama\t\t: {self.nama} \nNim \t\t: {self.nim}")
#5210411215
    #Method Overloading
    def hitungSks(self, jmlhsks = None, sks = None) :
        if jmlhsks != None and sks != None :
            totalsks = jmlhsks + sks
            print(f"Total sks\t: {totalsks}")
        else :
            totalsks = jmlhsks
            print(f"Total Sks\t: {totalsks}")

        if totalsks>=100 :
            print("Diperbolehkan mengambil skripsi")
        else :
            print("Tidak diperbolehkan mengambil skripsi")

mahasiswa1 = Mahasiswa("Eren", 123180015)
mahasiswa2 = Mahasiswa("Mikasa", 123190007)
#5210411215
mahasiswa1.tampilMhs()
mahasiswa1.hitungSks(80, 34)

mahasiswa2.tampilMhs()
mahasiswa2.hitungSks(83)

#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 6