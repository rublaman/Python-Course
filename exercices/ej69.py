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