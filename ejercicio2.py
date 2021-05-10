def sumar(n1,n2):
    return n1 + n2
n1 = float(input("Introduce un número: "))
n2 = float(input("Introduce otro número: "))
n3 = sumar(n1,n2)
if (n3==20):
    print ("Es igual")
else:
    print("No es igual")
if (n3>50):
    print("Te has pasado!")
else:
    print("Te has quedado corto!")
i = 1
while i < 6:
    print (i)
    i+=1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if (x=="banana"):
        print("encontrada banana")
    else:
        print("no encontrada")
