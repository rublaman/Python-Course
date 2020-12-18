
# Crea un programa que pregunte a traves de una interfaz grafica
# al usuario por texto. Al igual que el ej97 deberá de guardar y cerrar.

from tkinter import *       # Cargamos el módulo tk
from tkinter import ttk     # Cargamos ttk para widgests nuevos

fichero = open("exercices\\ficheros\\ej98.txt", "a+")

def add():
    fichero.write(entrada.get() + "\n")
    entrada.delete(0, END)

def save():
    global fichero
    fichero.close()
    fichero = open("exercices\\ficheros\\ej98.txt", "a+")

def close():
    fichero.close()
    root.destroy()

root = Tk()
root.title("Ejercicio 98")

valor_entrada = StringVar()
entrada = Entry(root, textvariable = valor_entrada)
entrada.grid(row = 0, column = 0)

boton_add = Button(root, text = "Añadir linea", command = add)
boton_add.grid(row = 0, column = 1)

boton_save = Button(root, text = "Guardar cambios", command = save)
boton_save.grid(row = 0, column = 2)

boton_close = Button(root, text = "Guardar y cerrar", command = close)
boton_close.grid(row = 0, column = 3)

root.mainloop()