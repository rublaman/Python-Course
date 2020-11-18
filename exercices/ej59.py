
# Por favor completa el codigo para que imprima la salida esperada

'''
Item 1 has index 0
Item 2 has index 1
Item 3 has index 2
'''

a = [1, 2, 3]

# Opcion nº1
'''
for n in a:
    print("Item {} has index {}".format(n, n-1))
'''
# Opcion nº2

for index, item in list(enumerate(a)):
    print("Item {} has index {}".format(item, index))