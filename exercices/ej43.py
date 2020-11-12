
# Crea un scrip que genera un fichero con las letras del alfabeto inglés
# y que esten unidas de dos en dos cada linea. 

'''
ab

cd

ef
'''

import string

list1 = string.ascii_lowercase[0::2]
list2 = string.ascii_lowercase[1::2]

with open("exercices\\ficheros\\ej43.txt", "w") as abecedario:
    for letra1, letra2 in zip(list1, list2):
        abecedario.write(letra1 + letra2 + "\n")
