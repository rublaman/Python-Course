
# En el fichero urls.txt tenemos varias direcciones erroenas
# Elimina la "s" de "https" y añade una barra. La salida correcta
# de las url seria:

'''
http://www.google.com
http://www.yahoo.com
http://www.stackoverflow.com
http://www.pythonhow.com
'''
rutaentrada = "exercices\\ficheros\\urls.txt"
rutasalida = "exercices\\ficheros\\ej94.txt"

with open(rutaentrada, "r") as fichentrada, \
    open(rutasalida, "w") as ficherosalida:
    for linea in fichentrada.readlines():
        url = linea.replace("s", "", 1)
        url = linea[:6] + "/" + linea[6:]
        ficherosalida.write(url)
