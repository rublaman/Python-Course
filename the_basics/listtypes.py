#---------------------------------------------------------------
# Las listas son una coleccion ordenadas y modificables.
#---------------------------------------------------------------

nota_estudiantes = [9.1, 6.0, 4.5, 3.3, 10.0, 5,6, 0.2, 4]
print(nota_estudiantes)

# Imprime segundo item
print("----Imprime segundo item----")
print(nota_estudiantes[1])

# Imprime usando index negativo
print("----Imprime usando index negativo----")
print(nota_estudiantes[-1])

# Rango de indices
print("----Rango de indices----")
print(nota_estudiantes[2:4])
print(nota_estudiantes[:4])
print(nota_estudiantes[3:])
print(nota_estudiantes[-4:-1])

# Cambio de valor
print("----Cambio de valor----")
nota_estudiantes[2] = 8.0
print(nota_estudiantes)

# Imprime todos los elemntos, uno por uno
print("----Imprime todos los elemntos, uno por uno----")
for n in nota_estudiantes:
    print(n)

# Comprobación si el item existe
print("----Comprobación si el item existe----")
if 10.0 in nota_estudiantes:
    print("Existe un 10")

# Añadir items con append()
print("----Añadir items----")
nota_estudiantes.append(7.7)
print(nota_estudiantes)

# Añadir item en X posicion con insert()
print("----Añadir item en X posicion----")
nota_estudiantes.insert(0, 5.5)
print(nota_estudiantes)

# Eliminar un item con remove()
print("----Eliminar un item----")
nota_estudiantes.remove(10.0)
print(nota_estudiantes)

# Eliminar el último item con pop()
print("----Eliminar el último item----")
nota_estudiantes.pop()
print(nota_estudiantes)

# Eliminar un index en especifico
print("----Eliminar un index en especifico----")
del nota_estudiantes[0]
print(nota_estudiantes)

# Eliminar la lista 
print("----Eliminar la lista----")
del nota_estudiantes

# Vaciar una lista
print("----Vaciar una lista----")
nota_estudiantes = [9.1, 6.0, 4.5, 3.3, 10.0, 5,6, 0.2, 4]
nota_estudiantes.clear()
print(nota_estudiantes)

# Copiar una lista
print("----Copiar una lista----")
nota_estudiantes = [9.1, 6.0, 4.5, 3.3, 10.0, 5,6, 0.2, 4]
nota_estudiantes2 = nota_estudiantes.copy()
print(nota_estudiantes2)

# Unir dos listas. Hay varias formas
print("----Unir dos listas----")
nota_estudiantes3 = nota_estudiantes + nota_estudiantes2
print(nota_estudiantes3)
del nota_estudiantes3

nota_estudiantes.extend(nota_estudiantes2)
print(nota_estudiantes)

# Metodos
print("----Metodos----")
print(list(map(lambda x: x*2, [1,2,3,4,5])))
print(list(filter(lambda x: x < 4, [1, 2, 10, 3, 20, 5, 4])))