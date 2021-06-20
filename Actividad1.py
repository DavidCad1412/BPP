import pandas as pd
import numpy as np

filename = 'finanzas2020.csv'
data = pd.read_csv(filename, delimiter=",")
df = pd.DataFrame(data)
x = print(df)

Mes= df.head(0)

for i in Mes:
    datos = data[i]
    print(datos)


data = pd.read_csv(filename, delimiter="\t")
df = pd.DataFrame(int(data))
x = print (df)


open('finanzas2020.csv', newline='') as csvfile:
