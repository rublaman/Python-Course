
# Crea una scrip que use los datos de countries_by_area.txt
# e imprima por pantalla los paises con mas densidad de poblacion.

import pandas as pd

poblacion = pd.read_csv("exercices\\ficheros\\countries-by-area.txt")

poblacion["densidad"] = poblacion["population_2013"] / poblacion["area_sqkm"]
poblacion = poblacion.sort_values('densidad', ascending = False)
print(poblacion)