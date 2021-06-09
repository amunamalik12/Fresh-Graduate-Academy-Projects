from operator import *
hijau = 5
kuning = 10
print('Kelereng Hijau = {}'.format(hijau))
print('Kelereng Kuning = {}'.format(kuning))
for func in (lt, le, eq, ne, ge, gt):
    print('{}(hijau, kuning): {}'.format(func.__name__, func(hijau, kuning)))
    #{} pertama untuk nama nama func dan {} kedua untuk hasil dari func (lt,le,eq...)
    #__name__ untuk memanggil nama func yang digunakan
