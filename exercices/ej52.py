
# Se supone que el codigo debe de pedir al usuario un nombre y apellido,
# y este lo imprima por pantalla. En lugar de eso lanza un error

'''
irstname = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" % firstname, secondname)
'''

firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is {} and your second name is {}".format(firstname, secondname))
