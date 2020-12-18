
# Escribe un script que pueda contrar e imprimir el 
# numero de ficheros .py en la carpeta ej92

import glob

ruta = "exercices\\ficheros\\ej92"

# Opción nº1
"""
ruta = "exercices\\ficheros\\ej92"
contador = 0

for fichero in glob.glob1(ruta, "*.py"):
    contador += 1

print(contador)
"""

# Opción nº2
lista = glob.glob1(ruta, "*.py")
print(len(lista))