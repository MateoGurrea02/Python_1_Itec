# Realizar un algoritmo que permita ingresar un dato numérico y determinar si es un número positivo de dos dígitos.
numero = int(input('Ingrese un numero: '))

if(numero >= 10 and numero < 100):
    print('El numero ingresado es positivo y de dos digitos')
else: 
    print('El numero ingresado es negativo o de un solo digito')
