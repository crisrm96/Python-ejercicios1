number=int(input('Dime un número entero: '))
number2= number+1
#y=str(number/number)
#z=str(number/1)
#k=range(1,number)
#x=number%3
#print(x)
for i in range(2,number):
        y = (number % i)
        #while i!=1 and number2:
        if y == 0:
            print('El número ' + str(number) + ' no es un número primo.')
            #print()
            break
        else:
            print('El número ' + str(number) + ' es primo.')
            break
#else:
 #   print('El número ' + str(number) + 'es primo.')        
        #if y == '1':
        #    print('Es un número primo.')
        #    if z == 'number':
        #        print('Es un número primo.')
        #elif x == '0':
        #    print('No es un número primo.')