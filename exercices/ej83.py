
# Crea un script que detecte la resolución de tu monitor

# Opcion nº1
'''
from win32.win32api import GetSystemMetrics

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))
'''

# Opcion nº2
from screeninfo import get_monitors

print("Altura = ", get_monitors()[0].height)
print("Anchura = ", get_monitors()[0].height)