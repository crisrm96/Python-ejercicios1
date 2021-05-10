diccionario = {'euro':'€','dollar':'$','yen':'¥'}
user=input('¿Qué divisa usas? ')
for e in diccionario:
    if user==e:
        print(diccionario[e])
        break
if user not in diccionario:
    print('Esta divisa ' + user + ' no se encuentra en el diccionario.')

#forma más facil de hacerlo:
if (user in diccionario):
    print(diccionario[user])
else:
    print('Esta divisa ' + user + ' no se encuentra en el diccionario.')    
