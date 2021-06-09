kata = 'bajingan'
kata = kata.upper()
print(kata)

kata1 = "AYAMKUNING"
kata1 = kata1.lower()
print(kata1)

print('    Kuahsoto'.lstrip())
print('    KuahMIE    '.lstrip())

kata2 = 'CodeCodeCodeCodeBAJINGANCodeCode'
print(kata2.strip('Code'))

print('Penghancur Dunia'.startswith('Penghancur'))
print('Penghancur Dunia'.endswith('Dunia'))

print(' '.join(['Peler','Kuda','sia goblog']))
print('ngab'.join(['Kamana','Gile','NGACO']))

print('Ayam Kampus !!'.split())
print('Ayamkampus123Unpad123!!'.split('123'))

print('''Halo,
aku cahyono
suka sekali mengamuk
tinggal di server dota
badanku imut dan suka menggeliat
senang era eru denganmu.'''.split('\n'))

string = "Ayo berkebon sama si Matilda di Pangalengan"
print(string.replace("Matilda","Nunung"))

string1 ="Mari berkebon sama si Matilda di Pangalengan karena di Pangalengan si Matilda suka Siomay"
print(string1.replace("Matilda","Nunung",2))

kata3 = 'KUCING'
print(kata3.isupper())

kata4 ='peler'
print(kata4.islower())

print('Kunyuk'.upper().lower())
print('Kunyuklicious'.lower().upper())
print('KUNYUKUS'.upper().lower().islower())
print('KUNYUKEA'.upper().lower().isupper())

print('sambel'.isalpha())
print('sambel123'.isalnum())
print('12345'.isdecimal())
print('   '.isspace())
print('Ayam Kuning'.istitle())


while True:
    print("Masukkan jumlah PELER ANDA: ")
    name = input()
    if name.isdecimal():
        print("Jumlah peler anda", name)
        break
    print('Masukkan jumlah peler anda yang benar.')


# Contoh 1: Penggunaan zfill 5 pada angka satuan
angka = 5
print (str(angka).zfill(5));
# Contoh 2: Penggunaan zfill 5 pada angka ratusan
angka = 300
print (str(angka).zfill(5));
# Contoh 3: Penggunaan zfill 5 pada angka desimal negatif (memiliki koma)
angka = -0.45
print (str(angka).zfill(5));
# Contoh 4: Penggunaan zfill 7 pada angka desimal negatif (memiliki koma)
angka = -0.45
print (str(angka).zfill(7));

# Contoh 1
kata = 'aku'
print (kata.zfill(5));
# Contoh 2
kata = 'kamu'
print (kata.zfill(5));
# Contoh 3
kata = 'dirinya'
print (kata.zfill(5));

print('PELERKUDA'.rjust(20))
print('PELERKUDA'.ljust(20))
print('PELERKUDA'.center(20))

print('PELERKUDUS'.ljust(20,'?'))
print('PELERKUDUS'.center(20,'-'))

print("Halo!\nKapan terakhir kali jokowi roll depan?\nteing goblog sigana mah Jum'at yang lalu.")

lineline = """ JAnCOK!
SIa reKK ku AIng KAdEKKK hAh?????
Dieu SIa LER"""
print(lineline)

print(r'Dicoding\tIndonesia') #karena rawstring maka ditampilkan apa adanya
