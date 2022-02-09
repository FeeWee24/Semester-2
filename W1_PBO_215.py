def LuasBalok(p,l):
    luas=p*l
    return luas
def VolumBalok(p,l,t):
    volum=LuasBalok(p,l)*t;
    return volum

p=float(input("panjang: "))
l=float(input("lebar: "))
t=float(input("tinggi: "))
print("Luas balok= ",LuasBalok(p,l))
print("Volume balok= ",VolumBalok(p,l,t))