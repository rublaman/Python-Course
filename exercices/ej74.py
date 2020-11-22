
# Concatena los dos ficheros en uno solo para que tengan esta salida.

'''
    x,y
    3,5
    4,9
    6,10
    7,11
    8,12
    6,10
    8,18
    12,20
    14,22
    16,24
'''

import pandas as pd

datos1 = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
datos2 = pd.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")

union = pd.concat([datos1, datos2])
union.to_csv("exercices\\ficheros\\ej74.txt", index = None)

# El metodo concat() espera como entrada una lista de objetos dataframe
# En la siguiente linea exportamos los datos a un fichero de teto