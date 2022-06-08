# 9)Dada una serie de números reales positivos, determinar el valor máximo y mostrarlo al final. Se deberá ir preguntando si hay más números para ingresar.


respuesta = input('Quieres ingresar un numero? Si/No: ')
numeroAntiguo = 0
while respuesta == 'Si':
  numero = float(input('Ingrese un numero real positivo: '))
  
  if numero > numeroAntiguo:
    numeroAntiguo = numero
    respuesta = input('Quieres otro numero? Si/No: ')
  else:
    respuesta = input('Quieres otro numero? Si/No: ')

print('El numero mayor es:', numeroAntiguo)