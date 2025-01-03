txt = 'Hello World'

print(txt)
# Menampilkan Jumlah Karakter
print(len(txt))

# Ambil Karakter Terakhir
print(txt[-1])

# Menampilkan huruf terakhir
print(txt[2:5])


# Hilangkan spasi pada text
print(txt.replace(' ',''))

#Ubah text menjadi huruf besar
print(txt.upper())

#ubah text menjadi huruf kecil
print(txt.lower())

# mengubah huruf H menjadi J
print(txt.replace('H','J'))

#LENGKAPI KODE BERIKUT!!

umur = 24
txt = 'Hello, nama saya rizki, dan umur saya adalah {} tahun'

print(txt.format(umur))
