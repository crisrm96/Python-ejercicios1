reply = "n"
while reply != "y":
    producto = input('¿Cómo se llama el producto que quiere comprar? ')
    precio = float(input('¿Cual es el precio del producto? '))
    unidades = input('¿Cuántas unidades quieres? ')
    preciotransf1 = round(precio,2)
    preciotransf2 = str(preciotransf1)
    preciotransf3 = preciotransf2.zfill(6)
    unidadestransf = unidades.zfill(3)
    print('El producto que has elegido es ' + producto + ' el precio unitario es de ' + preciotransf3 + ' euros, y tenemos ' + str(unidadestransf) + ' unidades. ¿Quiere comprarlo? ')
    preciototal = preciotransf1*float(unidadestransf)
    preciototaltransf1 = round(preciototal,2)
    preciototaltransf2 = str(preciototaltransf1)
    preciototaltransf3 = preciototaltransf2.zfill(8)
    reply = input('Type y or n: ')
    #reply == y
print ('El precio total de ' + str(unidadestransf) + ' unidades de ' + producto + ' es de ' + preciototaltransf3 + 'euros.')

   