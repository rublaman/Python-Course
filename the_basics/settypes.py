#---------------------------------------------------------------------
# Los set es una coleccion desorneada y no indexada. Se escribe con {}
# Al estar desordenada no podemos acceder a una posicion en concreto
#---------------------------------------------------------------------

colset = {"Ruben", "David", "Alberto"}
print(colset)

# Imprime todos los elemntos, uno por uno
print("----Recorremos la coleccion")
for n in colset:
    print(n)

# Comprobacion de un elemento
print("----Comprobamos la existencia de un elemento----")
print("Ruben" in colset)

# Añadir un elemento a la coleccion usando add()
colset.add("Mario")

# Añadir multiples elementos usando update()
colset.update([5, "Esther", 14])
print(colset)

# Elminar un elemento de la coleccion usando remove()
# Tambien podemos usar discard(), este metodo no da
# error si no encontramos el elemento en la coleccion
colset.remove("Ruben")
print(colset)

# Limpiar la coleccion usando el metodo clear()
colset.clear()
print(colset)

# Eliminar la coleccion usando del
colset = {"Ruben", "David", "Alberto"}
del colset

# Unir dos colecciones set. El metodo union() y
# el metodo update() excluiran duplicados
colset1 = {"Ruben", "David", "Alberto"}
colset2 = {123123, 7652, 9}
colset3 = colset1.union(colset2)
print(colset3)

# Metodo difference() e intersection()
set1 = {1,2,3,5}
set2 = {1,2,3,4,5}
print(set.intersection(set1, set2))
print(set.difference(set2, set1))