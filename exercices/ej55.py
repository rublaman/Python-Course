
# Agreaga un nuevo empleado al diccionario

d = {"employees":
        [{"firstName": "John", "lastName": "Doe"},
        {"firstName": "Anna", "lastName": "Smith"},
        {"firstName": "Peter", "lastName": "Jones"}],
"owners":
        [{"firstName": "Jack", "lastName": "Petter"},
        {"firstName": "Jessy", "lastName": "Petter"}]}

d["employees"].append({"firtName": "Ruben", "lastName": "Blanco"}) 

print(d)

# Tambien podemos usar 
'''
    d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
'''