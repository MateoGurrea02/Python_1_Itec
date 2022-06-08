#2)Preguntar si hay datos para ingresar, en caso afirmativo solicitar un número entero y decir si es negativo o no. Preguntar si repite.
respuesta = input('Quieres ingresar un número? Si/No: ')

while respuesta == 'Si':
    numero = int(input('Ingrese un número: '))
    if numero < 0:
        print('El número es negativo')
        respuesta = input('Quieres ingresar otro número? Si/No: ')
    else:
        print('El número es positivo')
        respuesta = input('Quieres ingresar otro número? Si/No: ')