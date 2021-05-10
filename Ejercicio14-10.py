userreply = int(input('¿Cuántos años tienes? '))
userreply2 = int(input('¿Cuánto dinero ingresas al mes? '))
if userreply < 16:
    print('Eres menor de edad, no tienes que tributar.')
else:
    if userreply2 < 1000:
        print('Ingresas menos de 1000 euros al mes, no tienes que tributar.')
    else:
        print('Tienes que tributar porque tienes ' + str(userreply) + ' años e ingresas más de 1000 euros al mes.')