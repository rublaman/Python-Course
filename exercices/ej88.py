
# Crea una scrip que use los datos de countries_by_area.txt
# e imprima por pantalla los paises con mas densidad de poblacion.

import pandas as pd

poblacion = pd.read_csv("exercices\\ficheros\\countries-by-area.txt")
poblacion["densidad"] = poblacion["population_2013"] / poblacion["area_sqkm"]
poblacion = poblacion.sort_values('densidad', ascending = False)

# Opción nº1
'''
paises = poblacion["country"]
paises = paises.head(5)
print(paises)
'''

# Opción nº2
for index, fila in poblacion[:5].iterrows():
    print(fila["country"])