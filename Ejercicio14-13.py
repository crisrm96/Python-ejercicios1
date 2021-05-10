numberuser = int(input('Dime un número entero positivo: '))
numberuser2 = numberuser-1
i=1
range_1= range(0,numberuser2)
for i in range_1:
    if i%2!=0:
        print(i , end=", ")
if numberuser%2!=0:
    print(numberuser)
else:
    print(numberuser2)
    
     


        

