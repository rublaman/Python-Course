
# Crea un script que genere un fichero con las letras del alfabeto inglés
# pero que estén de 3 en 3 en cada fila.

'''
abc

def

ghi
'''

import string

grupo1 = string.ascii_lowercase[0::3] + " "
grupo2 = string.ascii_lowercase[1::3] + " "
grupo3 = string.ascii_lowercase[2::3] + " "

with open("exercices\\ficheros\\ej44.txt", "w") as abecedario:
    for letra1, letra2, letra3 in zip(grupo1, grupo2, grupo3):
        abecedario.write(letra1 + letra2 + letra3 + "\n")

# Añadimos en grupo1, 2 y 3 un espacio en blanco ya que en el grupo1 y 3
# tendriamos longitud 9 y una con longitud 8.  