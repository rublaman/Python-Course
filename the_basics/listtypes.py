#---------------------------------------------------------------
# Para poder ver los metodos de las funciones usamos el comando
# dir(nombre_funcion). Si queremos conocer la información de los 
# métodos usamos el comando help(nombre_funcion.metodo)
#
# Para ver las funciones de python usamos dir(__builtins__)
# Las listas se crean con [] y pueden almacenar multiples tipos de
# variables
#---------------------------------------------------------------

nota_estudiantes = [9.1, 6.0, 4.5]
print(nota_estudiantes)

suma = sum(nota_estudiantes)
longitud = len(nota_estudiantes)
print(suma / longitud)