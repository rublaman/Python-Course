
# Usa Python para calcular la distnacia en kilometros entre 
# Jupiter y el sol el dia 1 de Enero de 1230

import ephem

distance_au_units = ephem.Jupiter('1230/1/1').sun_distance
distance_km = distance_au_units * 149597870.691
print(distance_km)