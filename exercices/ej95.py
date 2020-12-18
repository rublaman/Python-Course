
# Crea un script en el que insertando varias palabras separadas,
# por comas cree un fichero de texto. Cada palabra irá en una nueva linea.
# Si ejectuamos de nuevo el programa y añadimos una o varias palabras,
# tendrán que empezar donde la última palabra guardada anteriormente.

entrada = input("Introduce los valores: ")
entrada = entrada.split(",")

ruta = "exercices\\ficheros\\ej95.txt"

with open(ruta, "a+") as fichero:
    for linea in entrada:
        fichero.write(linea.replace(" ", "") + "\n")