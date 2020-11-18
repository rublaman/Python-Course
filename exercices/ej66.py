
# El programa toma una palabra del usuario como entrada y la
# traduce usando el siguiente diccionario

'''
d = dict(weather = "clima", earth = "terra", rain = "chuva") 
'''

d = dict(weather = "clima", earth = "terra", rain = "chuva")

# Opcion nº1
'''
def traducctor():
    entrada = input("Introduce una palabra: ")
    for clave, valor in d.items():
        if entrada == clave:
            print(valor)
            break

traducctor()
'''

# Opcion nº2
def traducctor(palabra):
    return d[palabra]

palabra = input("Introduce una palabra: ")
print(traducctor(palabra))
