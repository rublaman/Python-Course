
# Crea un diccionario de claves a, b, c donde cada clave tenga como valor una lista 
# de 1 a 10, 11 a 20 y 21 a 30 respectivamente. A continuación, imprima el diccionario 
# en un buen formato.

from pprint import pprint

d = dict(a = list(range(1,11)), b = list(range(11,21)), c = list(range(21, 31)))
pprint(d["b"][3])

# Usamos 3 listas con 3 rangos para crear el diccionario. Tambien importamos 
# pprint para dar formato a la salida 