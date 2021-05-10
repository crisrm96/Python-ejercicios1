amount = float(input('¿Cuánto dinero quieres invertir? '))
interes = float(input('¿Qué tipo de interés anual quieres? '))
years = int(input('¿Durante cuántos años quieres invertirlo? '))
amounttotal=amount
for i in range(0,years):
    interes1= (amounttotal*interes/100)
    amounttotal = amounttotal + interes1
    if i==0:
        print('Al cabo de ' + str(i+1) + ' año con el dinero que has invertido el primer año, obtendrías un total de ' + str(amounttotal) + ' euros.')
    else:
        print('Al cabo de ' + str(i+1) + ' años con el dinero que has invertido el primer año, obtendrías un total de ' + str(amounttotal) + ' euros.')