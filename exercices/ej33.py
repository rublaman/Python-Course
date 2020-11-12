
# ¿Cual será la salida del script? Intenta hacerlo mentalmente


c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())

# La variable c dentro de la funcion es una variable local. Las otras
# dos variables son globales y no tienen nada que hacer dentro de la
# funcion