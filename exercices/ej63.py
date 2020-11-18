
# Crea un programa que execute el programa una vez "Hola" instantaneamente,
# luego imprime "hola" despues de 1 segundo, luego 2 y 3 segundos. Entonces
# el programa imprimirá "Fin del bucle".

import time

i = 0

while True:
    print("Hello")
    i += 1
    if i > 3:
        print("Fin del bucle")
        break
    time.sleep(i)
