class Utama:
    def __init__(self):
        self._a = 2
        
class Turunan(Utama):
    def __init__(self):
        #memanggil konstruktor pada kelas utama
        Utama.__init__(self)
        print("memanggil variable protected pada class utama:",self._a)
        
        #memeodifikasi protected variable:
        self._a = 3
        print("memanggil variable protected yang dimodifikasi diluar class",self._a)

objek1 = Turunan()
objek2 = Utama()

#memanggil variable protected
print("mengakses variable protected dari objek1: ",  objek1._a)
print("mengakses variable protected dari objek2: ", objek2._a)