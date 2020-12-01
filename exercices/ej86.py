
# Con la siguiente lista  checklist = ["Portugal", "Germany", "Munster", "Spain"]
# uno de estos items no es un pais. Usa el fichoero countries-clean.txt como filtro
# de información para comprobar que item en la lista no es un pais. Una vez hayas 
# filtrado el elemento, tendremos que mostrar la lista limpia

# Opcion nº1
'''
checklist = ["Algeria", "Portugal", "Germany", "Munster", "Spain"]
ruta = 'exercices\\ficheros\\countries-clean.txt'
with open(ruta, 'r') as fichero:
    filtro = fichero.readlines()
    
filtro = [i.strip() for i in filtro if '\n' in i]

count = 0
for comprobacion in checklist:
    for pais in filtro:
        count += 1
        if comprobacion == pais:
            print('Pais encontrado: ', comprobacion)
            break
    
    if count == len(filtro):
        print('Borramos: ', comprobacion)
        checklist.remove(comprobacion)
        print('Borrado')

    count = 0
'''

# Opcion nº2
checklist = ["Algeria", "Portugal", "Germany", "Munster", "Spain"]
ruta = 'exercices\\ficheros\\countries-clean.txt'
with open(ruta, 'r') as fichero:
    filtro = fichero.readlines()

filtro = [i.strip() for i in filtro if '\n' in i]
filtrado = [i for i in filtro if i in checklist]

print(filtrado)
