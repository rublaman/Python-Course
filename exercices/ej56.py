
# Almacena el diccionario en un json

import json
d = {"employees":
     [{"firstName": "John", "lastName": "Doe"},
         {"firstName": "Anna", "lastName": "Smith"},
         {"firstName": "Peter", "lastName": "Jones"}],
     "owners":
     [{"firstName": "Jack", "lastName": "Petter"},
         {"firstName": "Jessy", "lastName": "Petter"}]}


with open("exercices\\ficheros\\company1.json", "w") as salida:
    json.dump(d, salida, indent = 4, sort_keys = True)

# Se ha creado un fichero json usando el metodo json.dump. El atributo sort_keys = true
# siver para presevar el orden del diccionario. El atributo intent = 4 crea 4 espacios en 
# blanco para aplicar sangria