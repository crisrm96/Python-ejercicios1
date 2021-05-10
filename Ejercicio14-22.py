dic = {}
reply= input('¿Desea comprar algo? ')
total = 0
if reply =='no':
    print('La lista de la compra está vacía.')
while reply =='yes':
    articulo = input('¿Qué quiere comprar? ')
    precio = input ('¿Cuánto cuesta? ')
    dic[articulo] = precio
    reply2 = input ('¿Desea comprar algo más? ')
    if reply2 !='yes':
        reply='no'
        print('A continuación le muestro la lista de la compra.')
        print('Lista de la compra')
        for k, v in dic.items():
            print(k + ' ' + v)
        for i in dic:
            total += float(dic[i])
        print('total ' + str(total))


        #     for value in dic:
        #         if value ==[0]:
        #             print('total ' + v)
        #         else:
        #             v = sumar (v,v)
        #             print('faalo ' + v)
        # #total3 = sum(item(articulo)) for item in dic
        # #print('total ' + str (total))
    

