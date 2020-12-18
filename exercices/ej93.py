
# El directorio ej93\subdirs contiene otros directorios dentro.
# Escribe un script para que cuente todos los ficheros .py dentro
# de todos los directorio

from glob import glob

ruta = ""

lista = glob("exercices\\ficheros\\ej93\\subdirs\\**\\*.py", recursive=True)
print(len(lista))