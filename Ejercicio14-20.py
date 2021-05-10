username= input('¿Cómo te llamas? ')
userage=input('¿Cuántos años tienes? ')
useradress=input('¿Cuál es tu dirección? ')
userphone=input('¿Cuál es tu número de telefono? ')
diccionario = {'nombre':username, 'edad':userage, 'direccion':useradress, 'telefono':userphone}
print(diccionario.get('nombre').capitalize() + ' tiene ' + diccionario.get('edad') + ' años, vive en ' + diccionario.get('direccion').capitalize() + ' y su numero de telefono es ' + diccionario.get('telefono'))
