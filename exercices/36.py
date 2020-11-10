
# Descarga el fichero words1.txt y crea una funcion python que
# idicando la ruta del fichero, lea el fichero, separe el contenido
# y # cuente los items 

# fichero = "the_basics\\texto.txt"

def leer_fichero(ruta):
    f = open(ruta, "r")
    return len(f.read().split())

print(leer_fichero("exercices\\ficheros\words1.txt"))