# Leer dos números y decir cuál es el mayor.
numero1 = float(input('Inserte un numero: '))
numero2 = float(input('Inserte otro numero: '))

if numero1 > numero2:
    print("Es mayor el numero", numero1)
elif numero1 == numero2:
    print("Los numeros son iguales")
else:
    print("Es mayor el numero", numero2)