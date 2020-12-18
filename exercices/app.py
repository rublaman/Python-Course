
# Crea un programa que pregunte al usuario por cualquier texto
# desde el navegador web. Cuando le demos al botón de guardar, este
# se deberá de guardar en un fichero de texto. Se recomienda usar Flask

# El fichero se llama app.py al usar el comando "python -m flask run"

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"