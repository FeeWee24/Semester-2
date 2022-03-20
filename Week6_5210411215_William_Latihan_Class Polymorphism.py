#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 6

#Polymorphism dengan Class
class kucing :
    def __init__(self, nama, umur) :
        self.nama = nama
        self.umur = umur
    
    def bersuara(self) :
        print("Meow")
#5210411215
class dog :
    def __init__(self, nama, umur) :
        self.nama = nama
        self.umur = umur
    
    def bersuara(self) :
        print("Guk...Guk...")

kucing1 = kucing("Tom", 3)
anjing1 = dog("Spike", 4)
#5210411215
for hewan in (kucing1, anjing1) :
    hewan.bersuara()
    
#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 6