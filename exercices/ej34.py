
# El siguiente script lanza NameError en la ultima linea indicando que
# "c" no está definida. Por favor, arregla la funcion para que la salida
# sea correcta

'''
def foo(): 
    c = 1 
    return c 
foo() 
print(c)
'''

def foo(): 
    global c
    c = 1 
    return c 
foo() 
print(c)

# Añadiendo global c arreglaria el codigo. Esa linea crea una variable
# c disponible para todo el codigo, aun estando dentro de la funcion