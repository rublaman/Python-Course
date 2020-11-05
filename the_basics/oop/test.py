# Programacion orientada a objetos

# clase: una coleccion de atributos que estan definidos para cualquier objeto

import math

class Complex:
    "esta clase simula numeros complejos"
    def __init__(self, real, imag):

        if(type(real) not in (int, float)) or type(imag) not in (int,float):
            raise Exception("Los argumentos no son numeros")
        
        self.__real = real
        self.__imag = imag

    def getReal(self):
        return self.__real

    def getImag(self):
        return self.__imag

    def getModulus(self):
        return math.sqrt(self.getReal() ** 2 + self.getImag() ** 2)

    def getPhi(self):
        return math.atan2(self.getReal(), self.getImag())

    def setReal(self, val):
        if type(val) not in (int, float):
            raise Exception("La parte real debe ser un numero")
        self.__real = val

    def setImag(self, val):
        if type(val) not in (int, float):
            raise Exception("La parte imag debe ser un numero")
        self.__imag = val


c = Complex(2.5, 3)

print(c.getModulus(), c.getPhi())

