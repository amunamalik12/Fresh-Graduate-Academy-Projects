contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]      #fungsi len() untuk menghitung panjang atau banyak elemen suatu list set maupun string
print(contoh_list)
print(len(contoh_list))

contoh_set = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(contoh_set)
print(len(contoh_set))

contoh_string = "Belajar Python"
print(contoh_string)
print(len(contoh_string))

angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]  # max() dan min() berfungsi untuk mengetahui nilai maksimal dan minimal
print(min(angka))
print(max(angka))

genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6)) # untuk melihat berapa jumlah 6 di list
string = "Makan sonice pake sayur kol gaenak banget bangsat"
substring = "a" # deklarasi variabel
print(string.count(substring)) # menghitung jumlah substring pada string

angka = [2, 4, 6, 8]
huruf = ['B', 'A', 'N', 'G', 'S', 'A','T']
gabung = angka + huruf
print(gabung)

learn = ['B', 'A', 'N', 'G', 'S', 'A','T']
replikasi = learn * 2
print(replikasi)

tujuh = [7]*5
print(len(tujuh))
print(tujuh)

for i in range(5): #deret dari 0 sampe n bilangan
    print(i)

for i in range(1, 11): #deret n,p ( n-p )
    print(i)

print([_ for _ in range(0,20,5)]) #range dengan metode n,p,q ( dari n-p dengan selisih q)

kalimat = "Belajar Python di Dicoding sangat menyenangkan"  #melihat apakah ada suatu substring pada string
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

data = ['shirt', 'white', 'L'] #klasifikasi data pada list
apparel = data[0]
color = data[1]
size = data[2]

data = ['shirt', 'white', 'L'] # From List
apparel, color, size = data
data = ('shirt', 'white', 'L')  # From Tuple
apparel, color, size = data

angka = [100, 1000, 500, 200, 5]
angka.sort() #sorting angka dr terkecil sampe terbesar
print(angka)

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort() #sort variabel kendaraan dari urutan alfabet
print(kendaraan)

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True) #sort variabel dari urutan alfabet, dan dibalik (reverse)
print(kendaraan)

 #urutan = ['Dicoding', 1, 2, 'Indonesia', 3] #tidak akan berjalan karena sort tidak dapat mengoperasikan angka dan string sekaligus
 #urutan.sort()
 #print(urutan)

kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort() #metode ini menggunakan ASCII maka string dengan awalan Kapital akan diprioritaskan
print(kendaraan)

kendaraan = ['Motor', 'Mobil', 'helikopter', 'pesawat']
kendaraan.sort(key=str.lower) #fungsi ini mengubah semua string menjadi non-kapital dan memperbaiki urutan alfabetik
print(kendaraan)
