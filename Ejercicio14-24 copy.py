import os
nif = {
    '05338098M' : {
        'nombre':'cristina',
        'direccion':'viriato',
        'telefono':'678234223',
        'correo':'crmoreiras2@gmail.com',
        'preferente':True
    },
    '00698113V': {
        'nombre':'margarita',
        'direccion':'galicia',
        'telefono':'798236723',
        'correo':'margarita@gmail.com',
        'preferente':False
    }
}

# user=input('¿Quiere añadir un cliente? (Type Y/N) ')
# if user =='Y':
user2='Y'
while user2 != 'end': 
    user2=input('¿Qué acción desea realizar? (Type add/remove/show/listall/listpref/end) ')
    #if user2 == 'add' and user2 == 'remove' and user2 == 'show' and user2 == 'listall' and user2 == 'listpref' and user2 == 'end':
    if user2 == 'add':
        user3= input('¿Cuál es su DNI? ')
        nif[user3]={}
        #nif = {k.replacce('05338098M', dni1): v}
        # nif('05338098M') = nif.pop(dni1)
        # nif('00698113V') = nif.pop(dni2)
        #nif= dict (dni1.items() + dni2.items() + user3.items())
        user3 = nif[user3]
        user4=input('¿Cuál es su nombre? ')
        user3['nombre']= user4
        user5=input('¿Cuál es tu direccion? ')
        user3['direccion']= user5
        user6= input('¿Cuál es tu telefono? ')
        user3['telefono']= user6
        user7= input('¿Cuál es tu correo? ')
        user3['correo']=user7
        user8=input('¿Eres cliente preferente? (Type Y/N) ')
        if user8 =='Y':
            user8=True
        else:
            user8=False
        user3 = {
            'nombre': user4,
            'direccion': user5,
            'telefono': user6,
            'correo': user7,
            'preferente':user8
        }
        user3['preferente']=user8
        for key in user3:
            if key=='preferente':
                if 'preferente' == False:
                    print('No es cliente preferente')
                else:
                    print('Es cliente preferente')
            else: 
                print (key, '=', user3[key])  
        #print(nif)      
    if user2 == 'remove':
        user9 = input('¿Qué número de DNI tiene el cliente que desea eliminar? ')
        del nif[user9]
        print('El cliente con número de DNI ' + user9 + ' se ha eliminado correctamente.')
    if user2 == 'show':
        user10=input('¿Qué número de DNI tiene el cliente que quiere ver? ')
        user10 = nif[user10]
        for key in user10:
            if key=='preferente':
                if 'preferente' == False:
                    print('No es cliente preferente')
                else:
                    print('Es cliente preferente')
            else: 
                print (key, '=', user10[key])
    if user2 =='listall':
        for key in nif:
            # if key =='preferente':
            #     if 'preferente'== False:
            #             print('No es cliente preferente')
            #     else:
            #             print('Es cliente preferente')
            # else: 
            for //Recorre el diccionario con todas las personas
                for //Para cada persona recorre sus campos
            if key == '05338098M':
                print (key, '-->')
                for k,v in nif ['05338098M'].items():
                    if k=='preferente':
                        if 'preferente'==False:
                            print('No es cliente preferente.')
                        else:
                            print('Es cliente preferente.')
                    else:
                        print('%s = %s' %(k,v))
            elif key == '00698113V':
                print (key, '-->')
                for k,v in nif ['00698113V'].items():
                    if k=='preferente':
                        if 'preferente'==False:
                            print('No es cliente preferente.')
                        else:
                            print('Es cliente preferente.')
                    else:
                        print('%s = %s' %(k,v))
            else:
                try:
                    user3
                    # if key ==user3:
                    for key in nif:
                        print("paco" + key)
                        print(user3)
                        if key == nif[]:
                            print (key, '-->')
                            for k,v in nif [user3].items():
                                if k=='preferente':
                                    if 'preferente'==False:
                                        print('No es cliente preferente.')
                                    else:
                                        print('Es cliente preferente.')
                                else:
                                    print('%s = %s' %(k,v))    
                except:
                    print('No hay más usuarios.')
            # if try==True:
            #     for key in nif:
            #         if key == user3:
            #             print (key, '-->')
            #             for k,v in nif [user3].items():
            #                 if k=='preferente':
            #                     if 'preferente'==False:
            #                         print('No es cliente preferente.')
            #                     else:
            #                         print('Es cliente preferente.')
            #                 else:
            #                     print('%s = %s' %(k,v))

            
            # for k,v in nif['00698113V'].items():
            #     print('%s = %s' %(k,v))
                #for k,v in nif[user3].items():
                    # print('%s = %s' %(k,v))
                #print(list(nif.values()))
    #print (nif['05338098M'])
    if user2 =='listpref':
        for key in nif:
            if nif[key]['preferente'] == True:
                print(nif[key])
                print('Este cliente es preferente.')
print('Muchas gracias, hasta pronto.')
#else:
    #print('No hay opciones disponibles.')
# else:
#     print ('Hasta pronto.')

