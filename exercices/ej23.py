
# Accede al tercer valor de la clave desde el diccionario. b

from pprint import pprint

d = dict(a = list(range(1,11)), b = list(range(11, 21)), c = list(range(21,31)))
print(d["b"][2])