# 11)Ingresar 7 números enteros y en el caso de que sean naturales de una sola cifra mostrar un cartel en cada uno.

for i in range(7):
    numero = int(input('Ingrese un numero: '))
    if numero < 10 and numero >= 0:
        print(numero)
    
