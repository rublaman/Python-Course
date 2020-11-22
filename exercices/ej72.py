# Crea un scrip que deje al usuario escribir cualquier palabra y 
# automaticamente se abra el navegador con el termino buscado en
# el motor de busqueda google

import webbrowser

busqueda = input("¿Que desea buscar?: ")
webbrowser.open_new("http://www.google.com/?#q={}".format(busqueda))