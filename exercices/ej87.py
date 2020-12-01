
# Coge la siguiente lista checklist = ["Portugal", "Germany", "Munster", "Spain"]  y 
# añade a la lista los paises de checklist

checklist = ["Portugal", "Germany", "Spain"]

with open('exercices\\ficheros\\countries-missing.txt', 'r') as fichero:
    lista = fichero.readlines()

lista = [i.strip() for i in lista if '\n' in i]
lista = lista + checklist
lista.sort()

with open('exercices\\ficheros\\countries-missing.txt', 'w') as fichero:
    for i in lista:
        fichero.write(i + '\n')