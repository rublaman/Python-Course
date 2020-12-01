
# Crea un scrip que pregunte al usuario por una contraseña y esta debe
# de tener al menos un número, al menos un caracter en mayuscula y con
# una longitud minima de 5 caracteres. Hay que dar la razón al usuario 
# por qué no se ha creado correctamente. Además se comprobará que no
# se repite el número de usuarios

ruta = "exercices\\ficheros\\ej81.txt"

def check_user(name, path):
    with open(path, "r") as usuarios:
        for usuario in usuarios:
            if name in usuario:
                return True
        return False

while True:
    notas = []
    usr = input("Introduza un usuario: ")
    if check_user(usr, ruta) is True:
        print("El usuario ya existe")
        continue
    psw = input("Introduza una contraseña: ")
    if not any(i.isdigit() for i in psw):
        notas.append("Necesita introducer al menos un digito")
    if not any(i.isupper() for i in psw):
        notas.append(">> Necesita al menos una letra mayusucula")
    if len(psw) < 5:
        notas.append(">> Necesita una contraseña con mas de 4 caracteres")
    if len(notas) == 0:
        print("El usuario y contraseña son correctos")
        break
    else:
        for nota in notas:
            print(nota)

# En la lectura de fichero podemos hacer una lista quitando los \n
'''
    users = file.readline()
    users = [i.strip("\n") for i in users]
'''