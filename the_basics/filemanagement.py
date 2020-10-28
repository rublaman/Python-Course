# open(ruta y nombre del fichero, acceso, buffer)

fichero = "the_basics\\texto.txt"

file = open(fichero, "r")
print(file.read())
file.close()

# Con read() indicamos el número de caracteres que queremos 
# leer y con tell() nos indica la posicion del puntero.
# El metodo seek() hace que podamos movernos a cualquier posicion
file = open(fichero, "r")
print(file.read(5), "posicion del puntero > ", file.tell())
print(file.read(3), "posicion del puntero > ", file.tell())
file.seek(2)
print("posicion del puntero > ", file.tell(), file.read(2))
file.close()

# Recorremos linea a linea con un bucle for
file = open(fichero, "r")
for linea in file:
    print(linea)

file.close()

# Metodo name() para mostar el nombre del fichero
file = open(fichero, "r")
print("Nombre del fichero de text: " + file.name)
print("esta cerrado: " + str(file.closed))

