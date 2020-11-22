
# Multiplica los valores que hay en la web *2 y almacenalos en
# un fichero de texto

import pandas

datos = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
datos = datos * 2
datos.to_csv("exercices\\ficheros\\ej73.txt", index = None)
