
# Crea un traductor de inglés a portugués que tome una palabra
# introducida por el usuario usando el siguiente diccionario y 
# además devuleva un mensaje si no se encuentra la palabra escrita
# dentro del diccionario

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# Opcion nº1
''' 
def traductor():
    entrada = input("Introduce una palabra: ")
    match = False
    for clave, valor in d.items():
        if clave == entrada:
            print(valor)
            match = True
            break
    if match == False:
        print("No se ha encontrado la palabra")

traductor()
'''

# Opcion nº2
'''
def traductor(palabra):
    return d[palabra]

try:
    palabra = input("Introduce una palabra: ")
    print(traductor(palabra))
except KeyError:
    print("No se ha encontrado la palabra")
'''

# Opcion nº3
def traductor(palabra):
    try:
        return d[palabra]
    except KeyError:
        return "No se ha encontrado la palabra"

palabra = input("Introduce una palabra: ")
print(traductor(palabra))