facturas = {}
total=0
userfac2 = input('¿Quiere hacer alguna acción? (Type Y/N) ')

while userfac2 =='Y': 
    total=0
    userfac=input('¿Qué acción desea realizar? (Type add/pay/exit) ')
    if userfac !='add' and userfac!= 'pay' and userfac!= 'exit':
        print('Esta acción no se encuentra disponible.')
    if userfac =='add':
        numero = input('¿Cuál es el número de la factura? ')
        valor = input('¿Cuánto cuesta la factura? ')
        facturas[numero]= valor
    elif userfac == 'pay':
        remove= input('¿Cuál es el número de factura? ')
        del facturas[remove]
    elif userfac == 'exit':
        userfac2 ='N'
    for i in facturas:
        total += float(facturas[i]) 
    print('Aún tienes que pagar ' + str(total) + ' euros.')
if userfac2 == 'N':
    print('Hasta pronto, muchas gracias.')