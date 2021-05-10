cliente = input('¿Quieres una pizza vegetariana? ')
Ingveg= ['pimiento', 'tofu']
Ingnoveg = ['peperoni', 'jamón', 'salmón']
if cliente =='yes':
    client = 'vegetariana'
    print(Ingveg)
else:
    print(Ingnoveg)
cliente = 'no vegetariana'
cliente2= input('¿Qué ingrediente quieres añadirle a tu pizza? ')
print('Perfecto, quieres una pizza ' + cliente + ' y añadirle el ingrediente ' +  cliente2)
