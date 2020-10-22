#---------------------------------------------------------------
# Para poder ver los metodos de las funciones usamos el comando
# dir(nombre_funcion). Si queremos conocer la información de los 
# métodos usamos el comando help(nombre_funcion.metodo)
#
# Para ver las funciones de python usamos dir(__builtins__)
#---------------------------------------------------------------

# Variables
x = 10
y = "10"
z = 10.3

# Operaciones
sum1 = x + x
sum2 = y + y 

# Strings
print(sum1,sum2)
print(type(x), type(y), type(z))
print("This is a {1} test. I'm {0} years old.".format("little", 28))
print("This is a {x} test. I'm {y} years old.".format(x = "prueba", y = 27))
print("This is a {x} test. I'm {0} years old. I like {1}".format(27, "code", x = "litte"))
print("{:b}".format(21))
print(r"c:\ruben\directory")
print("""\
    Hello:
            World
    """)
