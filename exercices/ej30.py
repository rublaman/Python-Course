
# ¿Por qué tenemos este error y como lo reparamos?

'''
def foo(a=2, b):
    return a + b
'''

def foo(b, a=2):
    return a + b

print(foo(3))

# Los argumentos por defecto deben estar detras de los 
# argumenos no por defecto