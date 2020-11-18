
# Crea un diccionario Inglés - Portugués. El programa debe de tomar
# como entrada una palabra del usuario y si no encuentra la palabra 
# deberá devolver la frase "No se ha encontrado esa palabra". Además 
# hay que hacer el programa "non case-sensitive". Esto quiere decir
# que si deberiamos dar por bueno "earth" y "Earth".

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

def traductor(palabra):
    try:
        return d[palabra.lower()]
    except KeyError:
        return "No se ha encontrado la palabra"
    
palabra = input("Introduza una palabra: ")
print(traductor(palabra))