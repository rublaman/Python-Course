# No hay una variable c definida antes de realizar la comparacion

a = 1
b = 2
print(a == b)
# print(b == c)

# Para remover los duplicados de una lista, lo que hacemos es convertir
# la lista en una coleccion set usando set() para quitarlos. Despues usando
# el metodo list() para volver a convertirlo a una listas

a = ["1", 1, "1", 2,4 ,4 ,4]
a = list(set(a))
print(a)

# Los diccionarios ordenados son otro tipo de datos, a diferencia de los 
# diccionarios normales, estos, estan ordenados.

from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

# Otra forma de elminar duplicados es usando un bucle for. Recorremos todos 
# los items de la lista para comprobar que no existen. Este algortimo puede tomar
# mucho tiempo si la lista es muy grande. No es recomendable usarlo.
a = ['2', 2, '2', 3]
b = list()

for i in a:
    if i not in b:
        b.append(i)

print(b)