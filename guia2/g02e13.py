# 13)Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y la cantidad de días que no llovió.
acumulador = 0
diasNoLlovidos = 0
for i in range(7):
  lluvia = input('Hoy llovio? Si/No: ')
  if lluvia == 'Si':
    milimetros = int(input('Cuanto llovio?(Ingrese la cantidad en milimetros): '))
    acumulador = acumulador + milimetros
  else:
    diasNoLlovidos = diasNoLlovidos + 1

print('La cantidad total de lluvia caida esta semana es de:', acumulador, 'mm y no llovio en', diasNoLlovidos, 'dias de la semana')