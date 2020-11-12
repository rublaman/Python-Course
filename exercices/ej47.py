
# Escribe un script que itere a traves de cada fichero del ej45 y compruebe
# si la letra dentro de esta es "python". Y ponga la letra del fichero en una lista
# si tiene en su interior "python"

import glob

rutas = glob.glob("exercices\\ficheros\\ej45\\*.txt")
lista = list()

for ruta in rutas:
    with open(ruta, "r") as txt:
        for palabra in txt:
            if "python" in palabra:
                lista.append(ruta[-5:-4])
        
print(lista)