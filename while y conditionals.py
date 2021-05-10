count = 0
banana = int(input('¿Cuántas bananas tengo?'))
if banana >= 100:
    print("I have a bunch of bananas")
elif banana > 1:
    print("I have a small bunch of bananas")
else:
    print ("I have no bananas")
while count <= 5:
    print("I have bananas!")
    count = count + 1
banana = int(input('¿Cuántas bananas tengo?'))