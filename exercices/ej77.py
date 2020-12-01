
# Crea un script que pregunte por la edad del usuario y calcule el
# año de nacimiento.

from datetime import datetime

edad = int(input("Por favor, introduza su edad: "))
year = datetime.now().year

print("Creo que usted ha nacido en el año {}".format(year - edad))