range_1 = range(10000,20000)
range_2 = range(20000,35000)
range_3 = range(35000,60000)
number= int(input('¿Cuánto ganas al año? '))
if number<10000:
    print('Te corresponde un tipo impositivo del 5%')
elif number in range_1:
    print('Te corresponde un tipo impositivo del 15%')
elif number in range_2:
    print('Te corresponde un tipo impositivo del 20%')
elif number in range_3:
    print('Te corresponde un tipo impositivo del 30%')
else:
    print('Te corresponde un tipo impositivo del 45%')