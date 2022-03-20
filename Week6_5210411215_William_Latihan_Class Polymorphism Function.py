#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 6

#Polymorphism dengan Fungsi
print(len("polymorphism"))
print(len([0, 1, 2]))
#5210411215
class jerman :
    def ibukota(self) :
        print("Berlin adalah ibukota negara Jerman")

class jepang :
    def ibukota(self) :
        print("Tokyo adalah ibukota negara Jepang")
#5210411215
negara1 = jerman()
negara2 = jepang()

for country in (negara1, negara2) :
    country.ibukota()
    
#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 6