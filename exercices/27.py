
# Crea una funcion que calcule la aceleracion dada por la velocidad
# inicial, velocidad final, tiempo inicial y tiempo final. Para
# comprobar la funcion, daremos el valor 0, 10, 0, 20 para v1, v2,
# t1 y t2 y debera generar una salida de 0.5

def aceleration_calc(v1, v2, t1, t2):
    return (v2 - v1) / (t2 - t1)

print(aceleration_calc(0,10,0,20))