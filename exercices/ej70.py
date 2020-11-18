
# Imprime el texto de esta web "http://www.pythonhow.com/data/universe.txt"

# Opcion nº1


import requests

r = requests.get('https://api.github.com/rublaman', auth=('user', 'pass'))
r.status_code

