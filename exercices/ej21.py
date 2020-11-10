
# Filtra el diccionario eliminando todos los items con un valor mayor a 1

d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)

# Creamos un nuevo diccionario con dict() recorriendo el diccionario "d".
# Si el valor es menor o igual que uno se copian en el nuevo diccionario