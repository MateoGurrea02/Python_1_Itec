# Leer dos números y luego una opción (puede ser '+' o '-'), y según la opción elegida realizar el cálculo.
numero1 = float(input('Ingrese un numero:'))
numero2 = float(input('Ingrese otro numero:'))

operacion = input('Que operacion quiere realizar:')

if operacion == '+':
    print('La suma de esos numeros es: ', numero1 + numero2)
elif operacion == '-':
    print('La resta de estos numeros es: ', numero1 - numero2)
