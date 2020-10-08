#--------------------------------------------------------------------------
# Las funciones de definen usando la palabra clave def
# Para llamar la funcion se escribe el nombre de esta seguido de parentesis
#--------------------------------------------------------------------------

nota_estudiantes = [9.1, 6.0, 4.5, 3.3, 10.0, 5,6, 0.2, 4]

def mi_funcion():
    print("Hola, esto es una funcion")

def medianotas(milista):
    milista = sum(milista) / len(milista)
    return milista

print(medianotas(nota_estudiantes))

# Llamada a una funcion con dos argumentos. Si llamamos a la
# funcion con 1 o 3 argumentos, obtendremos un error.
def mi_funcion2(nombre, apellido):
    print("Hola " + nombre + " " + apellido)

mi_funcion2("Ruben", "Blanco")

# El parametro *args se usa para un numero desconocido de argumentos posicionales.
# El parametro *args recibe los argumentos como una tupla
def suma(*nums):
    value = 0
    for n in nums:
        value += n
    return value

print(suma(2,3))

# El parametro **kwargs se usa para pasar de forma opcional a una funcion un numero de
# variables de argumentos con nombre. El parametro **kwargs recibe los argumentos como
# diccionario
