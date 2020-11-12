
# Crea una funcion que lea un texto como entrada y devuelva el numero
# de palabras. Considera que puede haber palabras separados por comas,
# como por ejemplo "Hi,it's me". 


def leer_fichero(ruta):
    f = open(ruta, "r")
    texto = f.read().replace(",", " ")
    return len(texto.split())

print(leer_fichero("exercices\\ficheros\words2.txt"))