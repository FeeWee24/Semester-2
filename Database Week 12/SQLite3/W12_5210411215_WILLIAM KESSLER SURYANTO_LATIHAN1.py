#WILLIAM KESSLER SURYANTO / 5210411215
import sqlite3
import os

connect = sqlite3.connect("Tabel Pegawai.db")

cur = connect.cursor()

# cur.execute("CREATE TABLE jabatan (kode_jabatan VARCHAR(3), nama_jabatan VARCHAR(30), gajipokok INT(10), tunjangan_jabatan INT(10))")
# cur.execute("CREATE TABLE pegawai (nip VARCHAR(20), nama_pegawai VARCHAR(40), kode_jabatan VARCHAR(3), kode_golongan VARCHAR(3), status VARCHAR(15), jumlah_anak INT(2))")
# cur.execute("CREATE TABLE gaji (bulan VARCHAR(20), nip VARCHAR(20), masuk INT(5), sakit INT(5), izin INT(5), alfa INT(5), lembur INT(5), potongan INT(10))")
# cur.execute("CREATE TABLE golongan (kode_golongan VARCHAR(3), nama_golongan VARCHAR(10), tunjangan_suami INT(10), tunjangan_anak INT(10), uang_makan INT(10), uang_lembur INT(10), askes INT(10))")

class Jabatan :
    def select() :
        try :
            sql = f"SELECT * FROM jabatan"
            cur.execute(sql)
            print(f"\nData Jabatan")
            print("==============================================")
            for x in cur.fetchall() :
                print(f"Kode Jabatan      : {x[0]}")
                print(f"Nama Jabatan      : {x[1]}")
                print(f"Gaji Pokok        : {x[2]}")
                print(f"Tunjangan Jabatan : {x[3]}\n") 
            print("==============================================\n\n")
            kembali()#5210411215
        except :
            print("\nEror")
            kembali()

    def search(kode_jabatan) :
        #try :
            cur.execute("SELECT * FROM jabatan  WHERE kode_jabatan LIKE ?", [kode_jabatan])
            print(f"\nHasil Pencarian Dari {kode_jabatan}")
            print("==============================================")
            for x in cur.fetchall() :
                print(f"Kode Jabatan      : {x[0]}")
                print(f"Nama Jabatan      : {x[1]}")
                print(f"Gaji Pokok        : {x[2]}")
                print(f"Tunjangan Jabatan : {x[3]}\n") 
            print("==============================================\n")
            kembali()

    def insert() :
        try :
            kode_jabatan = input("Masukan Kode Jabatan : ")
            nama_jabatan = input("Masukan Nama Jabatan : ")
            gpk = int(input("Masukan Gaji Pokok : "))
            tnj_jabatan = int(input("Masukan Tunjangan Jabatan : "))
            sql = ("INSERT INTO jabatan (kode_jabatan , nama_jabatan , gajipokok, tunjangan_jabatan) VALUES (?,?,?,?)")
            data = ( kode_jabatan, nama_jabatan, gpk, tnj_jabatan)
            cur.execute(sql,data)
            connect.commit()
            print ("\nData Berhasil Di Tambahkan")
            kembali()
        except :
            print ("\nEror / Data Tidak Berhasil Di Tambahkan")
            kembali()

    def update(kode_jabatan):
            cur.execute(f"SELECT * FROM jabatan WHERE kode_jabatan LIKE ?", [kode_jabatan])
            try :
                for x in cur.fetchall() :
                    if kode_jabatan in x[0] :
                        print("\n==============================================")
                        gpk = int(input("Masukan Gaji Pokok Baru\t: "))
                        tnj_jabatan = int(input("Masukan Tunjangan Baru\t: "))
                        sql = ("UPDATE jabatan SET gajipokok = ?, tunjangan_jabatan = ? WHERE kode_jabatan LIKE ?")
                        data = (gpk, tnj_jabatan, kode_jabatan)
                        cur.execute(sql, data)
                        connect.commit()
                        print(f"\nKode {kode_jabatan} Berhasil Di Edit")
                        print("==============================================")
                        print(f"Nama Jabatan\t\t: {x[1]}")
                        print(f"Gaji Pokok\t\t\t: {gpk}")  
                        print(f"Tunjangan Jabatan\t: {tnj_jabatan}")
                        print("==============================================\n")
                        kembali()
            except :
                print("\nData Tidak Berhasil Di Edit")
                kembali()#5210411215

    def delete(kode_jabatan):
        cur.execute(f"SELECT * FROM jabatan WHERE kode_jabatan LIKE ?", [kode_jabatan])
        try :
            for x in cur.fetchall() :
                if kode_jabatan in x[0] :
                    cur.execute(f"DELETE FROM jabatan WHERE kode_jabatan LIKE ?", [kode_jabatan])
                    connect.commit()
                    print(f"\n Kode {kode_jabatan} Berhasil Di Hapus")
                    kembali()
        except :
            print("Data Tidak Berhasil Di Hapus")
            kembali()

class Pegawai :
    def select() :
        try :
            sql = f"SELECT * FROM pegawai"
            cur.execute(sql)
            print(f"\nData Pegawai")
            print("==============================================")
            for x in cur.fetchall() :
                print(f"Nama Pegawai\t: {x[1]}")
                print(f"NIP\t\t: {x[0]}")
                print(f"Kode Jabatan\t: {x[2]}")
                print(f"Kode Golongan\t: {x[3]}")
                print(f"Status\t\t: {x[4]}")
                print(f"Jumlah Anak\t: {x[5]}")
            print("==============================================\n")
            kembali()
        except :
            print("\nEror")
            kembali()#5210411215

    def search(nip) :
        try :
            cur.execute(f"SELECT * FROM pegawai  WHERE nip LIKE ?", [nip])
            print(f"\nHasil Pencarian Dari {nip}")
            print("==============================================")
            for x in cur.fetchall() :
                print(f"Nama Pegawai\t: {x[1]}")
                print(f"NIP\t\t: {x[0]}")
                print(f"Kode Jabatan\t: {x[2]}")
                print(f"Kode Golongan\t: {x[3]}")
                print(f"Status\t\t: {x[4]}")
                print(f"Jumlah Anak\t: {x[5]}") 
            print("==============================================\n")
            kembali()
        except :
            print("\nEror")
            kembali()
            
    def insert() :
        try :
            nip = input("Masukan NIP\t\t: ")
            nama_pegawai = input("Masukan Nama Pegawai\t: ")
            kode_jabatan = input("Masukan Kode Jabatan\t: ")
            kode_golongan = input("Masukan Kode Golongan\t: ")
            status = input("Masukan Status\t\t: ")
            jmlh_anak = int(input("Masukan Jumlah Anak\t: "))
            sql = ("INSERT INTO pegawai (nip, nama_pegawai, kode_jabatan, kode_golongan, status, jumlah_anak) VALUES (?,?,?,?,?,?)")
            data = (nip, nama_pegawai, kode_jabatan, kode_golongan, status, jmlh_anak)
            cur.execute(sql,data)
            connect.commit()
            print ("\nData Berhasil Di Tambahkan")
            kembali()
        except :
            print ("\nEror / Data Tidak Berhasil Di Tambahkan")
            kembali()#5210411215

    def update(nip):
        cur.execute(f"SELECT * FROM pegawai  WHERE nip LIKE ?", [nip])
        try :
            for x in cur.fetchall() :
                if nip in x[0] :
                    print("\n==============================================")
                    kode_golongan = input("Masukan Kode Golongan baru\t: ")
                    status = input("Masukan Status Baru\t\t: ")
                    jmlh_anak = int(input("Masukan Jumlah Anak Baru\t: "))
                    sql = ("UPDATE pegawai SET kode_golongan = ?, status = ?, jumlah_anak = ? WHERE nip LIKE ?")
                    data = (kode_golongan, status, jmlh_anak, nip)
                    cur.execute(sql, data)
                    connect.commit()
                    print(f"\nNIP {nip} Berhasil Di Edit")
                    print("==============================================")
                    print(f"Nama Pegawai\t: {x[1]}")
                    print(f"NIP\t\t: {x[0]}")
                    print(f"Kode Jabatan\t: {x[2]}")
                    print(f"Kode Golongan\t: {kode_golongan}")
                    print(f"Status\t\t: {status}")
                    print(f"Jumlah Anak\t: {jmlh_anak}") 
                    print("==============================================\n")
                    kembali()
        except :
            print("\nData Tidak Berhasil Di Edit")
            kembali()

    def delete(nip):
        cur.execute(f"SELECT * FROM pegawai  WHERE nip LIKE ?", [nip])
        try :
            for x in cur.fetchall() :
                if nip in x[0] :
                    cur.execute("DELETE FROM pegawai WHERE nip LIKE ?", [nip])
                    connect.commit()
                    print(f"\nNIP {nip} Berhasil Di Hapus")
                    kembali()
        except :
            print("Data Tidak Berhasil Di Hapus")
            kembali()

class Gaji :
    def select() :
        try :
            sql = f"SELECT * FROM gaji"
            cur.execute(sql)
            print(f"\nData Gaji")
            print("==============================================")
            for x in cur.fetchall() :
                print(f"Bulan {x[0]}\t Nip {x[1]}")
                print(f"Masuk    : {x[2]}")
                print(f"Sakit    : {x[3]}")
                print(f"Izin     : {x[4]}")
                print(f"Alfa     : {x[5]}")
                print(f"Lembur   : {x[6]}")
                print(f"Potongan : {x[7]}\n") 
            print("==============================================\n")
            kembali()
        except :
            print("\nEror")
            kembali() #5210411215

    def search(nip) :
        try :
            cur.execute(f"SELECT * FROM gaji  WHERE nip LIKE ?", [nip])
            print(f"\nHasil Pencarian Dari {nip}")
            print("==============================================")
            for x in cur.fetchall() :
                print(f"Bulan {x[0]}\t Nip {x[1]}")
                print(f"Masuk    : {x[2]}")
                print(f"Sakit    : {x[3]}")
                print(f"Izin     : {x[4]}")
                print(f"Alfa     : {x[5]}")
                print(f"Lembur   : {x[6]}")
                print(f"Potongan : {x[7]}\n")  
            print("==============================================\n")
            kembali()
        except :
            print("\nEror")
            kembali()

    def insert() :
        try :
            bulan = input("Masukan Bulan\t\t: ")
            nip = input("Masukan NIP\t\t: ")
            masuk = int(input("Masukan Kehadiran\t: "))
            sakit = int(input("Masukan Data Sakit\t: "))
            izin = int(input("Masukan Data Izin\t: "))
            alfa = int(input("Masukan Data Alfa\t: "))
            lembur = int(input("Masukan Data Lembur\t: "))
            potongan = int(input("Masukan Potongan\t: "))
            sql = ("INSERT INTO gaji (bulan, nip, masuk, sakit, izin, alfa, lembur, potongan) VALUES (?,?,?,?,?,?,?,?)")
            data = (bulan, nip, masuk, sakit, izin, alfa, lembur, potongan)
            cur.execute(sql,data)
            connect.commit()
            print ("\nData Berhasil Di Tambahkan")
            kembali()
        except :
            print ("\nEror / Data Tidak Berhasil Di Tambahkan")
            kembali()

    def update(nip):
        cur.execute(f"SELECT * FROM gaji  WHERE nip LIKE ?", [nip])
        try :
            for x in cur.fetchall() :
                if nip in x[1] :
                    print("\n==============================================")
                    masuk = int(input("Masukan Kehadiran\t: "))
                    sakit = int(input("Masukan Data Sakit\t: "))
                    izin = int(input("Masukan Data Izin\t: "))
                    alfa = int(input("Masukan Data Alfa\t: "))
                    lembur = int(input("Masukan Data Lembur\t: "))
                    potongan = int(input("Masukan Potongan\t: "))
                    sql = ("UPDATE gaji SET masuk = ?, sakit = ?, izin = ?, alfa = ?, lembur = ?, potongan = ? WHERE nip LIKE ?")
                    data = (masuk, sakit, izin, alfa, lembur, potongan, nip)
                    cur.execute(sql, data)
                    connect.commit()
                    print(f"\nNIP {nip} Berhasil Di Edit")
                    print("==============================================")
                    print(f"Bulan {x[0]}\t Nip {x[1]}")
                    print(f"Masuk   : {masuk}")
                    print(f"Sakit   : {sakit}")
                    print(f"Izin    : {izin}")
                    print(f"Alfa    : {alfa}")
                    print(f"Lembur  : {lembur}")
                    print(f"Potongan : {potongan}\n")
                    print("==============================================\n")
                    kembali()
        except :
            print("\nData Tidak Berhasil Di Edit")
            kembali()

    def delete(nip):
        cur.execute(f"SELECT * FROM gaji  WHERE nip LIKE ?", [nip])
        try :
            for x in cur.fetchall() :
                if nip in x[1] :
                    cur.execute("DELETE FROM gaji WHERE nip LIKE ?", [nip])
                    connect.commit()
                    print(f"\nNIP {nip} Berhasil Di Hapus")
                    kembali()
        except :
            print("Data Tidak Berhasil Di Hapus")
            kembali()
    
class Golongan :
    # SELECT ALL
    def select() :
        try :
            sql = f"SELECT * FROM golongan"
            cur.execute(sql)
            print(f"\nData Golongan")
            print("==============================================")
            for x in cur.fetchall() :
                print(f"Kode golongan\t: {x[0]}")
                print(f"Nama Golongan\t: {x[1]}")
                print(f"Tunjangan suami\t: {x[2]}")
                print(f"Tunjangan Anak\t: {x[3]}")
                print(f"Uang Makan\t: {x[4]}")
                print(f"Uang Lembur\t: {x[5]}")
                print(f"Askes\t\t: {x[6]}")
            print("==============================================\n")
            kembali()
        except :
            print("\nEror")
            kembali()

    def search(nama_golongan) :
        try :
            cur.execute(f"SELECT * FROM golongan  WHERE nama_golongan LIKE ?", [nama_golongan])
            print(f"\nHasil Pencarian Dari {nama_golongan}")
            print("==============================================")
            for x in cur.fetchall() :
                print(f"Kode golongan\t: {x[0]}")
                print(f"Nama Golongan\t: {x[1]}")
                print(f"Tunjangan suami\t: {x[2]}")
                print(f"Tunjangan Anak\t: {x[3]}")
                print(f"Uang Makan\t: {x[4]}")
                print(f"Uang Lembur\t: {x[5]}")
                print(f"Askes\t\t: {x[6]}")
            print("==============================================\n")
            kembali()
        except :
            print("Gagal melakukan perintah")
            kembali()

    def insert() :
        try :
            kode_golongan = input("Masukan Kode Golongan\t: ")
            nama_golongan = input("Masukan Nama Golongan\t: ")
            tnj_suami = int(input("Masukan Tunjangan Suami\t: "))
            tnj_anak = int(input("Masukan Tunjangan Anak\t: "))
            uang_mkn = int(input("Masukan Uang Makan\t: "))
            uang_lbr = int(input("Masukan Uang Lembur\t: "))
            askes = int(input("Masukan Askes\t\t: "))
            sql = ("INSERT INTO golongan (kode_golongan, nama_golongan, tunjangan_suami, tunjangan_anak, uang_makan, uang_lembur, askes) VALUES (?,?,?,?,?,?,?)")
            data = (kode_golongan, nama_golongan, tnj_suami, tnj_anak, uang_mkn, uang_lbr, askes)
            cur.execute(sql,data)
            connect.commit()
            print ("\nData Berhasil Di Tambahkan")
            kembali()
        except :
            print ("Gagal melakukan perintah / Data Tidak Berhasil Di Tambahkan")
            kembali()

    def update(nama_golongan):
        cur.execute(f"SELECT * FROM golongan  WHERE nama_golongan LIKE ?", [nama_golongan])
        try :
            for x in cur.fetchall() :
                if nama_golongan in x[1] :
                    print("\n==============================================")
                    tnj_suami = int(input("Masukan Tunjangan Suami Baru\t: "))
                    tnj_anak = int(input("Masukan Tunjangan Anak Baru\t: "))
                    uang_mkn = int(input("Masukan Uang Makan Baru\t\t: "))
                    uang_lbr = int(input("Masukan Uang Lembur Baru\t: "))
                    sql = ("UPDATE golongan SET tunjangan_suami = ?, tunjangan_anak = ?, uang_makan = ?, uang_lembur = ? WHERE nama_golongan LIKE ?")
                    data = (tnj_suami, tnj_anak, uang_mkn, uang_lbr, nama_golongan)
                    cur.execute(sql, data)
                    connect.commit()
                    print(f"\nGolongan {nama_golongan} Berhasil Di Edit")
                    print("==============================================")
                    print(f"Nama Golongan\t: {x[1]}")
                    print(f"Tunjangan Suami\t: {tnj_suami}")
                    print(f"Tunjangan Anak\t: {tnj_anak}")
                    print(f"Uang Makan\t: {uang_mkn}")
                    print(f"Uang Lembur\t: {uang_lbr}") 
                    print("==============================================\n")
                    kembali()
        except : #5210411215
            print("\nData Tidak Berhasil Di Edit")
            kembali()

    def delete(nama_golongan):
        cur.execute(f"SELECT * FROM golongan  WHERE nama_golongan LIKE ?", [nama_golongan])
        try :
            for x in cur.fetchall() :
                if nama_golongan in x[1] :
                    cur.execute(f"DELETE FROM golongan WHERE nama_golongan LIKE ?", [nama_golongan])
                    print(f"\nGolongan {nama_golongan} Berhasil Di Hapus")
                    kembali()
        except :
            print("Data Tidak Berhasil Di Hapus")
            kembali()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def kembali():
    print("\n")
    input("Tekan tombol enter untuk kembali...")
    clear_screen() #5210411215

while True :
    clear_screen()
    print("1. Menu Jabatan")
    print("2. Menu Pegawai")
    print("3. Menu Gaji")
    print("4. Menu Golongan")
    print("0. Keluar")
    pilihan = input("Masukan Pilihan: ")
    if pilihan == '1' :
            clear_screen()
            print("============\t\t Menu Jabatan\t\t============")
            print("1. Tampil Jabatan")
            print("2. Tambah Jabatan")
            print("3. Cari Jabatan")
            print("4. Edit Jabatan")
            print("5. Hapus Jabatan")
            menu = input("Masukan Pilihan Menu: ")

            if menu == '1' :
                clear_screen()
                Jabatan.select()
            elif menu == '2' :
                clear_screen()
                Jabatan.insert()
            elif menu == '3' :
                clear_screen()
                Jabatan.search(kode_jabatan = input("Masukan Kode Jabatan: "))
            elif menu == '4' :
                clear_screen()
                Jabatan.update(kode_jabatan = input("Masukan Kode Jabatan yang ingin diubah: "))
            elif menu == '5' :
                clear_screen()
                Jabatan.delete(kode_jabatan = input("Masukan Kode Jabatan yang ingin dihapus: "))
        

    elif pilihan == '2' :
        try :
            clear_screen()
            print("============\t\t Menu Pegawai\t\t============")
            print("1. Tampil Pegawai")
            print("2. Tambah Pegawai")
            print("3. Cari Pegawai")
            print("4. Edit Pegawai")
            print("5. Hapus Pegawai")
            menu = input("Masukan Pilihan Menu: ")

            if menu == '1' :
                clear_screen()
                Pegawai.select()
            elif menu == '2' :
                clear_screen()
                Pegawai.insert()
            elif menu == '3' :
                clear_screen()
                Pegawai.search(nip = input("Masukan NIP: "))
            elif menu == '4' :
                clear_screen()
                Pegawai.update(nip = input("Masukan NIP yang inging diubah: "))
            elif menu == '5' :
                clear_screen()
                Pegawai.delete(nip = input("Masukan NIP yang ingin dihapus: "))
        except :
            clear_screen()
            print("Gagal melakukan perintah") #5210411215

    elif pilihan == '3' :
        try :
            clear_screen()
            print("============\t\t Menu Gaji\t\t============")
            print("1. Tampil Gaji")
            print("2. Tambah Gaji")
            print("3. Cari Gaji")
            print("4. Edit Gaji")
            print("5. Hapus Gaji")
            menu = input("Masukan Pilihan Menu: ")

            if menu == '1' :
                clear_screen()
                Gaji.select()
            elif menu == '2' :
                clear_screen()
                Gaji.insert()
            elif menu == '3' :
                clear_screen()
                Gaji.search(nip = input("Masukan NIP: "))
            elif menu == '4' :
                clear_screen()
                Gaji.update(nip = input("Masukan NIP yang ingin diubah: "))
            elif menu == '5' :
                clear_screen()
                Gaji.delete(nip = input("Masukan NIP yang ingin dihapus: "))
        except :
            clear_screen()
            print("Gagal melakukan perintah")

    elif pilihan == '4' :
        try :
            clear_screen()
            print("============\t\t Menu Golongan\t\t============")
            print("1. Tampil Golongan")
            print("2. Tambah Golongan")
            print("3. Cari Golongan")
            print("4. Edit Golongan")
            print("5. Hapus Golongan")
            menu = input("Masukan Pilihan Menu: ")

            if menu == '1' :
                clear_screen()
                Golongan.select()
            elif menu == '2' :
                clear_screen()
                Golongan.insert()
            elif menu == '3' :
                clear_screen()
                Golongan.search(nama_golongan = input("Masukan Nama Golongan: "))
            elif menu == '4' :
                clear_screen()
                Golongan.update(nama_golongan = input("Masukan Nama Golongan yang ingin diubah: "))
            elif menu == '5' :
                clear_screen()
                Golongan.delete(nama_golongan = input("Masukan Nama Golongan yang ingin dihapus: "))
        except :
            clear_screen()
            print("Gagal melakukan perintah")

    elif pilihan == '0' :
        clear_screen() #5210411215
        break

#WILLIAM KESSLER SURYANTO / 5210411215