#---------------------------------------------------------------------
# Para poder ver los metodos de las funciones usamos el comando
# dir(nombre_funcion). Si queremos conocer la información de los 
# métodos usamos el comando help(nombre_funcion.metodo)
#
# Son desordenados, modificables e indexados
#---------------------------------------------------------------------

nota_estudiantes = {
    "Ruben": 7.7,
    "David": 8.3, 
    "Rodrigo": 6.0
}

# Imprime las claves con keys() y los valores con values()
print(nota_estudiantes.keys())
print(nota_estudiantes.values())

# Acceso a un valor
print("----Acceder a un valor----")
print(nota_estudiantes["Ruben"])

# Cambio de variables
print("----Cambio de variables----")
nota_estudiantes["Ruben"] = 6.0
print(nota_estudiantes)

# Imprime las claves a traves de un bucle for
print("----Imprime las claves----")
for n in nota_estudiantes:
    print(n)

# Imprime los valores a traves de un bucle for
# Forma nº1
print("----Imprime los valores (forma 1)----")
for n in nota_estudiantes:
    print(nota_estudiantes[n])

# Forma nº2
print("----Imprime los valores (forma 2)----")
for n in nota_estudiantes.values():
    print(n)

# Imprime los valores y las claves usando items()
for x, y in nota_estudiantes.items():
    print(x, y)

# Comprobacion de si existe la clave
print("----Comprobacion de si existe la clave----")
if "Ruben" in nota_estudiantes:
    print("Si, Ruben esta en el diccionario")

# Añadir item al diccionario
print("----Añadir item al diccionario----")
nota_estudiantes["Sergio"] = 5.5
print(nota_estudiantes)

# Eliminar un item
print("----Eliminar un item----")
nota_estudiantes.pop("Sergio")
print(nota_estudiantes)

# Vacir el diccionario con el metodo clear()
print("----Vacir el diccionario----")
nota_estudiantes.clear()
print(nota_estudiantes)

# Copiar un diccionario
print("----Copiar un diccionario----")
nota_estudiantes = {
    "Ruben": 7.7,
    "David": 8.3, 
    "Rodrigo": 6.0
}
nota_estudiantes2 = nota_estudiantes.copy()
print(nota_estudiantes2)

# Anidar diccionarios dentro de otro diccionario
print("----Anidar diccionarios dentro de otro diccionario----")
notas = {
    "Programacion"  : {
        "Ruben"     : 7.0,
        "David"     : 10.0,
        "Sergio"    : 4.5,
    },
    "Calculo"       : {
        "Ruben"     : 8.9,
        "David"     : 5.0,
        "Sergio"    : 8.0,
    }
}
print(notas)
