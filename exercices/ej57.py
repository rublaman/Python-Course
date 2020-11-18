
# JSON a diccionario. Usa json y pprint

import pprint
import json

with open("exercices\\ficheros\\company1.json", "r") as json_file:
    diccionario = json.load(json_file)

pprint.pprint(diccionario)