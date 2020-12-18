
# Escribe un programa que pregunte al usuario en bucle texto. Para
# parar la solicitud tendrá que escribir "CERRAR"

ruta = "exercices\\ficheros\\ej96.txt"

# Opción nº1
'''
while True:
    entrada = input("Escribe un valor: ")
    if entrada == "CERRAR":
        break
    
    with open(ruta, "a+") as fichero:
        fichero.write(entrada + "\n")
'''

# Opción nº2

file = open(ruta, "a+")

while True:
    entrada = input("Introduce text: ")
    if entrada == "CERRAR":
        file.close()
        break
    else:
        file.write(entrada + "\n")