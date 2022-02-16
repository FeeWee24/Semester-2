#5210411215 William Kessler Suryanto

#Membuat list
merk_hp = ('apple', 'samsung', 'huaweii', 'xiaomi', 'vivo')
print(merk_hp)
#Mengubah list menjadi set
merk_hp = set(['apple', 'samsung', 'huaweii', 'xiaomi', 'vivo'])
print(merk_hp)
#Membuat Set dengan berbagai tipe data
set_merkhp = {'samsung', 'galaxy', 24, True, ('A', 'B')}
print(set_merkhp)

print("")
himpunan_huruf = {'a', 'b', 'c'}
print(himpunan_huruf)
#Fungsi Add
himpunan_huruf.add('d')
himpunan_huruf.add('e')
print(himpunan_huruf)
#Fungsi Update
himpunan_huruf.update({ 'f', 'g' })
print(himpunan_huruf)

print("")
himpunan = {'william', 'andi', 100, ('a', 'b'), False, True}
print(himpunan)
#Fungsi Remove
himpunan.remove(100)
print(himpunan)
#Fungsi Discard
himpunan.discard(('a', 'b'))
print(himpunan)
#Fungsi Pop
nilaiYangDihapus = himpunan.pop()
print('nilaiYangDihapus =', nilaiYangDihapus)
print(himpunan)
#Fungsi Clear
himpunan.clear()
print(himpunan)

grup_laki = {
  'andi', 'budi', 'joko', 'argus'
}
grup_perempuan = {
  'putri', 'ajeng', 'cia', 'feli'
}
print("")
#Fungsi Union (Gabungan)
print(grup_laki.union(grup_perempuan))
#Fungsi Intersection (Irisan)
print(grup_laki.intersection(grup_perempuan))
#Fungsi Difference (Selisih)
print('\nanggota grup laki yang bukan anggota grup perempuan')
print(grup_laki - grup_perempuan)
print(grup_laki.difference(grup_perempuan))

print('\ndibalik, anggota grup perempuan yang bukan anggota grup laki:')
print(grup_perempuan - grup_laki)
print(grup_perempuan.difference(grup_laki))
#Symmetric Difference
print('\nanggota yang hanya ikut satu grup saja:')
print(grup_perempuan.symmetric_difference(grup_laki))

#5210411215 William Kessler Suryanto
