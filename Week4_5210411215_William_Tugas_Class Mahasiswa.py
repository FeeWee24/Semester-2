#WILLIAM KESSLER SURYANTO
#PBO VII
#5210411215

class Mahasiswa :
    def __init__ (self, nama, nim, prodi, semester, sks) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.__semester = semester
        self.__sks = sks

mahasiswa1 = Mahasiswa("William", "5210411215", "Informatika",2, 22)
mahasiswa2 = Mahasiswa("Dicka", "5210411229", "Informatika", 2, 22)
mahasiswa3 = Mahasiswa("Havin", "5210411212", "Informatika", 2, 23)
mahasiswa4 = Mahasiswa("Rifqi", "5210411211", "Informatika", 2, 24)

mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("List Mahasiswa Informatika")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {}. Saat ini sudah Semester {}, dengan mengambil mata kuliah {} SKS.'. format(mhs.nama, mhs.prodi, mhs.nim, mhs._Mahasiswa__semester, mhs._Mahasiswa__sks)
    print(teks)
print("\n")
