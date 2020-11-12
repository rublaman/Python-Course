
# ¿Por qué hay un error en el codigo y como se podria arreglar?

'''
def foo(a, b):
    print(a + b)
 
x = foo(2, 3) * 10
'''

# No se puede multplicar oprque la funcion no devuelve nada.
# Para arreglarlo necesitamos un return

def foo(a, b):
    return(a + b)

x = foo(2, 3) * 10
print(x)
