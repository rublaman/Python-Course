
# Crea un scrip que genere un fichero de texto con todas las letras del
# alfabeto ingles, cada letra en una linea distinta

# Forma nº1
'''
import string

f = open("exercices\\ficheros\ej41.txt", "w")
for letra in string.ascii_lowercase:
    f.write(letra + "\n")
'''

# Forma nº2

import string

with open("exercices\\ficheros\ej41.txt", "w") as abecedario:
    for letra in string.ascii_lowercase:
        abecedario.write(letra + "\n")