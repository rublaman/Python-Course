
# Escribe una funcion que calcule el volumen liquido de una esfera, 
# usando la siguiente formula. El radio "r" es siempre 10, podemos
# considerarlo un parametro por defecto

from math import pi

def volumen(h, r = 10):
    v = ((4 * pi * r**3) / 3) - ((pi * h**2 * (3*r - h)) / 3)
    return v

print(volumen(2))