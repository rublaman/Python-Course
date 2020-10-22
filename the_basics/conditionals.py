# Igual: a == b
# Distinto de: a != b
# Menor que: a < b
# Menor o igual que: a <= b
# Mayor que: a > b
# Mayor o igual que: a >= b
# Cominar AND: and
# Operador OR: or

a = 200
b = 400
c = 300
d = 50

# if, elif y else
if b > a:
    print("b es mayor que a")
elif a == b:
    print("los valores son iguales")
else:
    print("a es menor que b")

# Forma corta de expresar la condicion if
if a > b: print("a es mayor que b")

# Forma corta con if, else
print("A") if a > b else print("B")

# Operador AND
if a < b and c > d:
    print("Las dos condiciones son ciertas")

# Operador OR
if a < b or c < d:
    print("Al menos una condicion es cierta")

# La declaracion pass. Se usa para cuando una declaracion
# no puede estar vacia y no tenemos contenido para insertar
if a > b:
    pass
