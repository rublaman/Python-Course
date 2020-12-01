
# Crea un scrip que pregunte al usuario por una contraseña y esta debe
# de tener al menos un número, al menos un caracter en mayuscula y con
# una longitud minima de 5 caracteres. Hay que dar la razón al usuario 
# por qué no se ha creado correctamente

while True:
    notas = []
    psw = input("Introduza una contraseña: ")
    if not any(i.isdigit() for i in psw):
        notas.append(">> Necesitas al menos un número")
    if not any(i.isupper() for i in psw):
        notas.append(">> Necesitas al letra mayuscula")
    if len(psw) < 5:
        notas.append(">> La contraseña debe tener mas de 5 caracteres")
    if len(notas) == 0:
        print("La contraseña es correcta!")
        break
    else:
        for nota in notas:
            print(nota)