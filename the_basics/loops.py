for i in range(2, 10):
    print(i)

string = "Cadena de texto"
for i in range(len(string)):
    print(i)

for char in string:
    print(char)

print("")
for i in range(1,11):
    print("{:<3}|".format(i), end="")

    for j in range(1, 11):
        print("{:<4}".format(i*j), end="")

    if i == 1:
        print("\n{:#^42}".format(""),end="")

    print("")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)