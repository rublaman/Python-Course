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