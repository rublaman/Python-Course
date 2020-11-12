
# Crea un script que genere 26 ficheros de texto con el nombre a.txt, b.txt
# hasta la z. Cada fichero debe conetener una letra reflejando su nombre
# de fichero. En el fichero a.txt debe de estar la letra a.

# Opcion nº 1
'''
import string

for letra in string.ascii_lowercase:
    with open("exercices\\ficheros\\ej45\\{}.txt".format(letra), "w") as fichero:
        fichero.write(letra + "\n")
'''

# Opcion nº 2
import string, os

if not os.path.exists("exercices\\ficheros\\ej45"):
    os.makedirs("exercices\\ficheros\\ej45")

for letra in string.ascii_lowercase:
    with open("exercices\\ficheros\\ej45\\{}.txt".format(letra), "w") as fichero:
        fichero.write(letra + "\n")