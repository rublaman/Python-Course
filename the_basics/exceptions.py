print("----Primer try except----")
try:
    n = int(input("Introduce un entero: "))
except:
    print("Eso no es un numero entero")

print("----Segundo try except----")
try:
    sum = 0
    file = open("numero.txt", "r")
    for numero in file:
        sum = sum + 1.0 / int(numero)
    print(sum)
except ZeroDivisionError:
    print("Numero en el fichero es igual a cero")
except IOError:
    print("Fichero no encontrado")



print("----raise----")
a = 1

def raise_exception(a):
    if type(a) != type("a"):
        raise ValueError("Esto no es una cadena")

try:
    raise_exception(a)
except ValueError as e:
    print(e)



# Assert es una instrucción que debe cumplirse siempre,
# si no se cumple, interrumpira el programa y volcará 
# una traza señalando el punto donde el assert falló.
print("----assert----")
def comparar_num(a, b):
    assert a < b, "a es mayor que b"

try:
    comparar_num(8, 4)
except AssertionError as e:
    print(e)