x = 100
print('Nilai x adalah', x)
print('hai {}'. format('bro'))

nama = "Dicoding"
umur = 5
print("Halo, %s!" % nama)
print("Umur %s adalah %d tahun." %(nama, umur))

angka = [7, 9, 11, 13]
print("Angka saya: %s" % angka)

a, b = 10, 11
a, b
print('a: %x and b: %X' % (a, b))

nilai = input('Masukkan angka : ')
print(nilai)
print(float(nilai))
# print(int('90+10')) tidak akan bekerja karena int() maupun float() tidak dapat memproses ekspresi matematis, gunakan eval()
print(eval('90+10'))
