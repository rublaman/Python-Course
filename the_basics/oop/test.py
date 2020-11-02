# Programacion orientada a objetos

# clase: una coleccion de atributos que estan definidos para cualquier objeto

class Complex:
    "esta clase simula numeros complejos"
    def __init__(self, real, imag):

        if(type(real) not in (int, float)) or type(imag) not in (int,float):
            raise Exception("Los argumentos no son numeros")
        
        self.real = real
        self.imag = imag

try:
    c = Complex(2, "a")
    print(c.real, c.real)
except Exception as e:
    print(e)

