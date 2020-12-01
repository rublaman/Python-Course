
# Crea un script que genere una contraseña con 6 caracteres alfanumericos.

import secrets
import string

alfabeto = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
password = "".join(secrets.choice(alfabeto) for i in range(6))
print(password)