
# El fichero ej85.txt contiene una lista con paises, pero
# ademas contiene texto inncesario entre los paises. Limpia
# la lista con Python genreando un nuevo fichero txt que contenta 
# una lista limpia

# Opcion nº1 
'''
import string

ruta = 'exercices\\ficheros\\ej85.txt'
abc = list(string.ascii_uppercase)

with open(ruta, 'r') as fichero:
    paises = fichero.readlines()
    paises = [i.strip('\n') for i in paises]
    paises = list(filter(None, paises))

    for linea in paises:
        if (linea in abc):
            paises.remove(linea)

    with open('exercices\\ficheros\\ej85salida.txt', 'w') as fichero:
        for linea in paises:
            fichero.write(linea + '\n')
'''

# Opcion nº2

with open('exercices\\ficheros\\ej85.txt', 'r') as fichero:
    contenido = fichero.readlines()

contenido = [i.strip('\n') for i in contenido if '\n' in i]
contenido = [i for i in contenido if i != '']
contenido = [i for i in contenido if i != 'Top of Page']
contenido = [i for i in contenido if len(i) != 1]

with open('exercices\\ficheros\\ej85salida.txt', 'w') as fichero:
    for pais in contenido:
        fichero.write(pais + '\n')