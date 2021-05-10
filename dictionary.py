diccionario = {"color":"verde", "tamaño":"grande", "forma":"ovalada", "peso":20}
print(diccionario["color"])
print(diccionario.get("forma"))
#abajo estás creando un diccionario dentro de otro, estas creando un diccionario dentro de color.
diccionario2 = {"color":{"azul":2, "verde":3, "amarillo":7}}
#abajo estás imprimiendo el valor de un diccionario dentro de otro
print(diccionario2["color"]["verde"])
