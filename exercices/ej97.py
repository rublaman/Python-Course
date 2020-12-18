
# Crea un programa que pregunte al usuario para insertar texto 
# repetidamente. El programa guardará los cambios cuando el usuario
# escriba GUARDAR, pero no se cerrará el programa. El programa se
# cerrará y guardará los cambios cuando el usuario escriba CERRAR

ruta = "exercices\\ficheros\\ej97.txt"
fichero = open(ruta, "a+")

while True:
    entrada = input("Introduce texto: ")
    if entrada == "GUARDAR":
        fichero.close()
        fichero = open(ruta, "a+")
    elif entrada == "CERRAR":
        fichero.close()
        break
    else:
        fichero.write(entrada + "\n")
    
