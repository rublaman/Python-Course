
# Crea una fucion que tome cualquier string y que de como salida
# el numero de palabras

def count_string(text):
    palabras = text.split(" ")
    return len(palabras)

print(count_string("Me llamo Ruben"))

# El metodo split() crea una lista con los caracteres separados y
# usando el metodo len() en la lista podemos ver el numero de valores
# que hay dentro