import pandas as pd #import library pandas

path_to_file = "E:\PhytonProject\dicoding academy\Minggu2/contohawal.csv"  #setting alamat data dari directory

contohawal = pd.read_csv(path_to_file) #baca data yang udah diimpor dr atas

print(contohawal.head()) #ngeprint header data
print(contohawal.shape) #ngasih tau bentuk data segede apa
print(contohawal.dtypes) #ngasih tau tipe data untuk tiap kolom

url = "http://users.stat.ufl.edu/~winner/data/resid_energy.dat"
data_energi = pd.read_csv(url, sep=r"\s+", header = None) #sep=r"\s+" digunain biar setiap ada space dianggep kolom baru, terus tambahin header = None kalo gaada header kolom
print(data_energi.head())
print(data_energi.shape)
print(data_energi.dtypes)
