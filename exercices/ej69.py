# Crea un fichero vacio y nombralo requests.py. Luego copia
# el siguiente código

'''
    import requests
    
    r = requests.get("http://www.pythonhow.com")
    print(r.text[:100])
'''

import requests
import pprint

r = requests.get("http://www.google.com")
pprint.pprint(r.text[:400])

# print(r.status_code)

# Con status_code el cliente nos indica si la peticion ha sido recibida y aceptada
# Si sale 200 es que la recepción es correcta
