#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 8

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="william2411"
)
curl = conn.cursor()

def tambah_buku():
    judul= input("Masukan Judul Buku\t\t= ")
    subjek= input("Masukan Jenis Buku\t\t= ")
    lokasi= input("Masukan Lokasi Buku\t\t= ")
    info= input("Masukan Info Buku\t\t= ")
    isbn= input("Masukan ISBN Buku\t\t= ")
    pengarang= input("Masukan Author Buku\t\t= ")
    jumlahhal= input("Masukan Jumlah Halaman Buku\t= ")
    ukuran= input("Masukan Ukuran Buku\t\t= ")
    rating= input("Masukan Rating Buku\t\t= ")
    curl.execute("INSERT INTO infobuku(judul,subjek,lokasi,info,isbn,pengarang,jumlahhal,ukuran,rating) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(judul,subjek,lokasi,info,isbn,pengarang,jumlahhal,ukuran,rating))
    print("Tambah Buku Berhasil!")
#5210411215    
def tambah_majalah():
    judul= input("Masukan Judul Majalah\t\t= ")
    subjek= input("Masukan Jenis Majalah\t\t= ")
    lokasi= input("Masukan Lokasi Majalah\t\t= ")
    info= input("Masukan Info Majalah\t\t= ")
    volume= input("Masukan Volume Majalah\t\t= ")
    issue= input("Masukan Issue Majalah\t\t= ")
    curl.execute("INSERT INTO infomajalah(judul,subjek,lokasi,info,volume,issue) VALUES(%s,%s,%s,%s,%s,%s)",(judul,subjek,lokasi,info,volume,issue))
    print("Tambah Majalah Berhasil!")
    
def tambah_dvd():
    judul= input("Masukan Judul DVD\t\t= ")
    subjek= input("Masukan Jenis DVD\t\t= ")
    lokasi= input("Masukan Lokasi DVD\t\t= ")
    info= input("Masukan Info DVD\t\t= ")
    aktor= input("Masukan Aktor Utama DVD\t\t= ")
    genre= input("Masukan Genre DVD\t\t= ")
    rating= input("Masukan Rating DVD\t\t= ")
    curl.execute("INSERT INTO infodvd(judul,subjek,lokasi,info,aktor,genre,rating) VALUES(%s,%s,%s,%s,%s,%s,%s)",(judul,subjek,lokasi,info,aktor,genre,rating))
    print("Tambah DVD Berhasil!")

def tampil_buku() :
    sql = f"SELECT * FROM infobuku"
    curl.execute(sql)   
    print(f"\nData Buku")   
    print("==============================================")
    for x in curl.fetchall() :
        print(f"Judul : {x[0]}")
        print(f"Pengarang : {x[5]}")
        print(f"Jumlah Halaman : {x[6]}")
        print(f"Kategori : {x[1]}\n") 
    print("==============================================\n\n")
#5210411215
def tampil_majalah() :
    sql = f"SELECT * FROM infomajalah"
    curl.execute(sql)   
    print(f"\nList Majalah")
    print("==============================================")
    for x in curl.fetchall() :
        print(f"Judul : {x[0]}")
        print(f"Volume : {x[4]}")
        print(f"Issue : {x[5]}")
        print(f"Kategori : {x[1]}\n") 
    print("==============================================\n\n")

def tampil_dvd() :
    sql = f"SELECT * FROM infodvd"
    curl.execute(sql)
    print(f"\nList DVD")
    print("==============================================")
    for x in curl.fetchall() :
        print(f"Judul : {x[0]}")
        print(f"Aktor : {x[4]}")
        print(f"Genre : {x[5]}")
        print(f"Kategori : {x[1]}\n") 
    print("==============================================\n\n")
#5210411215
def cari_buku(judul) :
    sql = f"SELECT * FROM infobuku WHERE judul LIKE '%{judul}%'"
    curl.execute(sql)
    print(f"\nHasil Pencarian dari {judul}")
    print("==============================================")
    for x in curl.fetchall() :
        print(f"Judul : {x[0]}")    
        print(f"Letak : {x[2]}")
        print(f"Status : {x[3]}\n") 
    print("==============================================\n\n")

def cari_majalah(judul) :
    sql = f"SELECT * FROM infomajalah WHERE judul LIKE '%{judul}%'"
    curl.execute(sql)
    print(f"\nHasil Pencarian dari Majalah dengan judul{judul}")
    print("==============================================")
    for x in curl.fetchall() :
        print(f"Judul : {x[0]}")
        print(f"Letak : {x[2]}")    
        print(f"Status : {x[3]}\n") 
    print("==============================================\n\n")
#5210411215
def cari_dvd(judul) :
    sql = f"SELECT * FROM infodvd WHERE judul LIKE '%{judul}%'"
    curl.execute(sql)
    print(f"\nHasil Pencarian dari DVD dengan judul {judul}")
    print("==============================================")
    for x in curl.fetchall() :
        print(f"Judul : {x[0]}")
        print(f"Letak : {x[2]}")
        print(f"Status : {x[3]}\n") 
    print("==============================================\n\n")
            
while True :
    print("=======================\n    SEARCH ITEM \n=======================")
    print("1. Menu Buku ")  
    print("2. Menu Majalah")
    print("3. Menu DVD")
    print("4. Menu Tambah")
    print("0. selesai")
    menu = input("Pilihan Menu : ") 

    if menu == '1' :
        print("1. Tampil Buku")
        print("2. Cari Buku")
        pilihan = input("Pilihan : ")  

        if pilihan == '1' :
            tampil_buku()  
        elif pilihan == '2' :              
            judul = input("Masukan Judul Buku\t: ")
            cari_buku(judul)
#5210411215            
    elif menu == '2' :
        print("1. Tampil List Majalah")
        print("2. Cari Majalah")
        pilihan = input("Pilihan : ")  

        if pilihan == '1' :
            tampil_majalah()  
        elif pilihan == '2' :              
            judul = input("Masukan Judul Majalah\t: ")
            cari_majalah(judul)
#5210411215
    elif menu == '3' :
        print("1. Tampil List DVD")
        print("2. Cari DVD")
        pilihan = input("Pilihan : ")  

        if pilihan == '1' :
            tampil_dvd()  
        elif pilihan == '2' :              
            judul = input("Masukan Judul DVD\t: ")
            cari_dvd(judul)

    elif menu == '4' :
        print("1. Tambah Buku")
        print("2. Tambah Majalah")
        print("3. Tambah DVD")
        pilihan = input("Pilihan : ")
        
        if pilihan == '1' :
            tambah_buku()
        elif pilihan == '2' :
            tambah_majalah()
        elif pilihan == '3' :
            tambah_dvd()
            
    elif menu == '0' : 
        print("Terima Kasih\n")
        break

    else : 
        print("Pilihan tidak tersedia")
#5210411215
#WILLIAM KESSLER SURYANTO
#PBO-7 WEEK 8
