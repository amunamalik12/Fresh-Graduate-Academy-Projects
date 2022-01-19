import pandas as pd #import library pandas
from io import StringIO
import csv

path_to_file = "E:\PhytonProject\dicoding academy\Minggu2/contohkedua.csv"  #setting alamat data dari directory

contohawal = pd.read_csv(path_to_file)#baca data yang udah diimpor dr atas

df=contohawal

df["Bajingan"] = 1 + 4
df["Manusia;Belalang;Kucing;Ayam"] = df["Manusia;Belalang;Kucing;Ayam"] + 'goblok lu semua' + 'BANGSAT'
df["Setan"] = 88
df["Bajingan"] = df["Bajingan"].astype("float")
df["Setan"] = df["Setan"].astype("float")

print(df.head()) #ngeprint header data
print(df.shape) #ngasih tau bentuk data segede apa
print(df.dtypes) #ngasih tau tipe data untuk tiap kolom
print(pd.get_dummies(df["Manusia;Belalang;Kucing;Ayam"]))
