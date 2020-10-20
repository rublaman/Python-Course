#---------------------------------------------------------------------
# Una tupla es una coleccion ordenada e inmutable. Se escriben con ()
# No podemos ni añadir ni eliminar elementos una vez creada la tupla,
# pero si podemos unir varias tuplas
#---------------------------------------------------------------------

notastupla = (10, 3, 33, 54, 67, 58)
notastupla2 = ("hola", "333", 75)
print(notastupla)

# Acceso a tuplas
print("----Acceso a tuplas----")
print(notastupla[1])

# Rango de indices
print("----Rango de indices----")
print(notastupla[-1])

# Imprime usando un rango
print(notastupla[2:5])

# Imprime usando rangos negativos
print(notastupla[-4:-1])

# Imprime todos los elemntos, uno por uno
print("----Imprime todos los elemntos, uno por uno----")
for n in notastupla:
    print(n)

# Unir dos tuplas
print("----Union de dos tuplas----")
notastupla3 = notastupla +  notastupla2
print(notastupla3)