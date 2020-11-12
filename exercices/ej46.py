
# Escribe un script que extraiga la letra de cada fichero del ejercicio 45
# y lo insertes en una lista. Usa glob.glob para crear la lista de las rutas
# de los ficheros y luego itera atraves de la lista leyendo el contenido de 
# cada fichero

import glob

lista = list()

for ruta in glob.glob("exercices\\ficheros\\ej45\\*.txt"):
    with open(ruta, "r") as txt:
        lista.append(txt.read().strip("\n"))

print(lista)
