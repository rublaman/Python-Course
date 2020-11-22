
# Cuenta el número de caracteres "a" que hay en el texto dentro de
# http://www.pythonhow.com/data/universe.txt

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get("http://www.pythonhow.com/data/universe.txt", headers = headers)

# Opcion nº1 Bucle for y condicion if para comprobar el nº de "a"
'''
count = 0
for caracter in r.text:
    if caracter == "a":
        count += 1

print(count)
'''

# Opcion nº2 Metodo count() de un string para contar el nº de "a"
texto = r.text
print(texto.count("a"))