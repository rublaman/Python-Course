def fact(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * fact(x-1))


num = 3
print("El factorial de", num, "es", fact(num))