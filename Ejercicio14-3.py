ahorros1año = int(input ('Escribe el dinero que depositas el primer año '))
print('Depositas ' + str(ahorros1año) + ' euros.')
dinerointereses1 = ahorros1año*4/100
ahorros1añototal = ahorros1año + dinerointereses1
print('Te dan ' + str(round(dinerointereses1,2)) + ' euros por intereses, por lo que tienes ' + str(round(ahorros1añototal,2)) + ' euros de ahorro en total el primer año.')
dinerointereses2 = ahorros1añototal*4/100
ahorros2añototal = dinerointereses2 + ahorros1añototal
print('Te dan ' + str(round(dinerointereses2,2)) + ' euros por intereses, por lo que tienes ' + str(round(ahorros2añototal,2)) + ' euros de ahorros en total el segundo año.')
dinerointereses3 = ahorros2añototal*4/100
ahorros3añototal = dinerointereses3 + ahorros2añototal
print('Te dan ' + str(round(dinerointereses3,2)) + ' euros por intereses, por lo que tienes ' + str(round(ahorros3añototal,2)) + ' euros de ahorros en total el tercer año.')