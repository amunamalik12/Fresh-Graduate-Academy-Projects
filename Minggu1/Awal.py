print("Hello World")

a = 10                          #deklarasi
print(a, "type is", type(a))       #menunjukkan tipe

b = 1.7
print(b, "type is", type(b))

c = 1+3j
print(b, "type is complex?", isinstance(1+3j,complex))      #yes/no untuk complex number

x = [5, 10 ,15 ,20 ,30 ,35 ,40]   #list
print ( x[5] )  #ngambil elemen ke -
print ( x[-1])  #ngambil elemen terakhir
print (x[3:5]) #buat list buat indeks 3-4 (tanpa 5)
print (x[:5]) #buat elemen dr indeks pertama kecuali 5
print (x[-3:]) #buat elemen dr indeks ketiga dr blakang smpe akhir
print (x[1:7:2]) #buat elemen dr indeks pertama sampe 6 dengan step 2
