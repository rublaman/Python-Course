
# El script debe de imprimir por pantalla 
# "Hoy es dia de la semana, dia mes, año"

from datetime import datetime

print(datetime.now().strftime("Today is %A, %B %d, %Y"))