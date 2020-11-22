
# Muestra los datos en un gráfico recogiendo los datos de la
# URL http://www.pythonhow.com/data/sampledata.txt

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
print(datos)
plt.plot(datos["x"], datos["y"], "ro")
plt.show()