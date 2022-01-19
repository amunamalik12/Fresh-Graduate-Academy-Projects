from pydataset import data
import pandas as pd
print(data())

BOD = data('BOD')

print(BOD.head())
print(BOD.dtypes)
print(BOD.shape)
