
# Usa el fichero ten-more-contries.txt para añadir a la base de datos,
# database.db 10 paises mas.

import sqlite3
import pandas as pd

data = pd.read_csv("exercices\\ficheros\\ten-more-countries.txt")

print(type(data))

conn = sqlite3.connect('exercices\\ficheros\\database.db')
c = conn.cursor()

data.to_sql("countries", conn, if_exists="append", index=False)