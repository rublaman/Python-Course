
# Usa Python para mostrar en pantalla los paises con una area mas
# grande que 2,000,000. Luego expotalo a un fichero CSV.

import sqlite3
import pandas as pd

conn = sqlite3.connect('exercices\\ficheros\\database.db')
c = conn.cursor()

c.execute("SELECT * FROM countries WHERE area >= 2000000")
filas = c.fetchall()
c.close()

df = pd.DataFrame.from_records(filas)
df.columns = ["Rango", "Pais", "Area", "Poblacion"]
df.to_csv("exercices\\ficheros\\ej90.csv", index=False)