
# El codigo produce un error. Intenta compernder el error y reparalo

'''
age = input("What's your age? ")
age_last_year = age - 1
print("Last year you were %s." % age_last_year)
'''

# Opcion nº1

age = int(input("What's your age? "))
age_last_year = int(age) - 1
print("Last year you were %s." % age_last_year)

# Opcion nº2

age = input("What's your age? ")
age_last_year = int(age) - 1
print("Last year you were %s." % age_last_year)

# La funcion input siempre devuelve un string. Podemos arregarlo
# convirtiendo la variable age a entero con int() o tambien en
# la funcion input