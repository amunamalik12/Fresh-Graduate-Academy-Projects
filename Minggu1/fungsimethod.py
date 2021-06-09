def kali(angka1, angka2): #deklarasi fungsi dan parameter
    # Kalikan kedua parameter
    hasil = angka1 * angka2
    return hasil

# Panggil fungsi kali
keluaran = kali(10, 20);
print('Dicetak sebagai kembalian: {}'.format(keluaran))

def kuadrat(x):
    hasil = x*x
    
a = 10
k = kuadrat(a)
print('nilai kuadrat dari {} adalah {}'.format(a, k))

def ubah(list_aku):
    "Deklarasi Variabel list_saya berikut hanya dikenali (berlaku) di dalam fungsi ubah"
    list_aku = [1, 2, 3, 4]
    print ('Nilai di dalam fungsi: {}'.format(list_aku))

# Panggil fungsi ubah
list_saya = [10, 20, 30]
ubah(list_saya)
print('Nilai di luar fungsi: {}'.format(list_saya))

def printinfo(*args, **kwargs): #position argument * #keyword argument **
    for a in args:
        print('argumen posisi {}'.format(a))
    for key, value in kwargs.items():
        print('argumen kata kunci {}:{}'.format(key, value))


# Panggil printinfo
printinfo()
printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
printinfo(*(2, 3), **{'i':7, 'j':8})

#impor
import hello
#panggil
hello.world()

#cetak
print(hello.nama)
#review
cahyo = hello.Reviewer("cahyo", "Python")
cahyo.review()
