
# Usa Python para mostrar en pantalla los paises con una area mas
# grande que 2,000,000 

import sqlite3

conn = sqlite3.connect('exercices\\ficheros\\database.db')
c = conn.cursor()

# Opcion nº1
'''
for fila in c.execute('SELECT country FROM countries WHERE area > 2000000'):
    print(fila)
'''
# Opcion nº2
c.execute('SELECT * FROM countries WHERE area >= 2000000')
filas = c.fetchall()
conn.close

for i in filas:
    print(i[1])