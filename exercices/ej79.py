
# Crea un scrip que pregunte al usuario por una contraseña y esta debe
# de tener al menos un número, al menos un caracter en mayuscula y con
# una longitud minima de 5 caracteres.

# Opción nº1
'''
mayus = False
numero = False
longitud = False
incorrecto = True

while incorrecto:
    password = input("Por favor, introduza una nueva contraseña: ")

    for letra in password:
        if letra.isupper():
            mayus = True
        if letra.isdigit():
            numero = True
        if len(password) > 4:
            longitud = True

    if letra and numero and longitud:
        incorrecto = False
        print("La contraseña es correcta")
    else:
        print("La contraseña no es correcta")
'''

# Opción nº2
while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")