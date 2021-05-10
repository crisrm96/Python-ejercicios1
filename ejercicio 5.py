import random
n=random.randint(1,1)
nu=int(input('Dime el número que crees que he elegido'))
while nu!=n:
    if nu>n:
        nu=int(input('El numero es más pequeño'))
    elif nu<n:
        nu=int(input('El numero es más grande'))
print('Felicidades has adivinado que el numero secreto es:', n)
