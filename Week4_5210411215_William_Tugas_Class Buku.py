#WILLIAM KESSLER SURYANTO
#PBO VII
#5210411215

class Buku :
    def __init__(self, judul,pengarang, tahun_terbit, chapter) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__chapter = chapter

buku1 = Buku("Juujika no Rokunin", "Nakatake Shiryuu", 2020, 55)
buku2 = Buku("Shounen no Abyss", "Minenami Ryou", 2020, 268)
buku3 = Buku("Oshi no Ko", "Akasaka Aka", 2020, 194)

buku_manga = [buku1, buku2, buku3]
print("List Buku Manga")
for buku in buku_manga :
    teks = 'Buku Manga {} karangan {} pertama kali diterbitkan tahun {} dan manga ini dirilis sudah mencapai total {} chapter'.format(buku.judul, buku.pengarang, buku.tahun_terbit, buku._Buku__chapter)
    print(teks) 
print("\n")