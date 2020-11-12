
# Imprime el apellido del segundo empleado

d = {"employees":   
        [{"firstName": "John", "lastName": "Doe"},
        {"firstName": "Anna", "lastName": "Smith"},
        {"firstName": "Peter", "lastName": "Jones"}],
    "owners":       
        [{"firstName": "Jack", "lastName": "Petter"},
        {"firstName": "Jessy", "lastName": "Petter"}]}

print(d["employees"][1]["lastName"])


# d['employees'] devuelve esta listas

'''
    [{"firstName": "John", "lastName": "Doe"},
    {"firstName": "Anna", "lastName": "Smith"},
    {"firstName": "Peter", "lastName": "Jones"}]
'''

# d['employees'][1]  devuelve el segundo item de la lista anterior

'''
    {"firstName": "Anna", "lastName": "Smith"}
'''