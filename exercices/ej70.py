
# Imprime el texto de esta web "http://www.pythonhow.com/data/universe.txt"

# Opcion nº1


import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get("http://www.pythonhow.com/data/universe.txt", headers = headers)
print(r.text)
print(r.status_code)

# Con status_code el cliente nos indica si la peticion ha sido recibida y aceptada
# Si sale 200 es que la recepción es correcta
