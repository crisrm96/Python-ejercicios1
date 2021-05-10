def sumar (x,y):
    return x + y
x = 2
y = 4
z = sumar(x,y)
print(z)
def restar (x,y):
    return x - y
x = 4
y = 7
z = restar (x,y)
print (z)
def multiplicar (x,y):
    return x + y
x = 5
y = 7
z = multiplicar (x,y)
print(z)
def dividir (x,y):
    return x / y
x = 3
y = 2
z = dividir(x,y)
print(z)
def funcionb (q):
    print("llegas a funcionb " + str (q))
a = 3
b = 5
funcionb (sumar(a,b))
