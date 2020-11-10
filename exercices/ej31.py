
# ¿Por que hay un error en este codigo y como lo puedes arreglar?

'''
def foo(a=1, b=2):
    return a + b
 
x = foo - 1
'''

def foo(a=1, b=2):
    return a + b


print(type(foo()))
x = foo() - 1
print(x)