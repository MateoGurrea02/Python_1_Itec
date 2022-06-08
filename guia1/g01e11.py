# El costo del pasaje a Córdoba es de $2000. 
# La empresa realiza un descuento de un 40 % sobre el costo del boleto a los niños que tienen entre 5 y 10 años y a los jubilados (mayores de 65). 
# Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.

precioPasaje = 2000
pasajeDescuento = precioPasaje - (precioPasaje * (40 / 100))
nombre = input('Ingrese su nombre:')
edad = int(input('Ingrese su edad:'))

if ((edad <= 10 and edad >= 5) or edad >= 65):
    print(nombre, 'El valor final de su pasaje es de:', pasajeDescuento)
else:
    print(nombre, 'El valor final de su pasaje es de:', precioPasaje)