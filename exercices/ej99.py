
# Crea un programa que pregunte al usuario por cualquier texto
# desde el navegador web. Cuando le demos al botón de guardar, este
# se deberá de guardar en un fichero de texto. Se recomienda usar Flask

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"