
# Usa python para añadir un nuevo empleado al fichero JSON
# Primero creamos el diccionario con json.loads(), añade el 
# nuevo par de claves y valores y con file.seek(0) pon el 
# cursor en la parte superior del fichero y entonces vuelva 
# el diccionario al archivo abierto de nuevo

import json
import pprint

with open("exercices\\ficheros\\company1.json", "r+") as fichero_json:
    diccionario = json.load(fichero_json)
    diccionario["employees"].append({"firstName": "John", "lastName": "Bert"})
    fichero_json.seek(0)
    json.dump(diccionario, fichero_json, indent = 4, sort_keys = True)
    fichero_json.truncate()

 # seek(0) sirve para poner el cursor arriba del todo en el fichero json.

    




