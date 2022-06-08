# 5)Pedir los montos de sueldos de los empleados de una empresa hasta que no haya más y mostrar el total.

respuesta = 'Si'
acumulador = 0

while respuesta == 'Si':
    if respuesta == 'Si':
      sueldo = int(input('Ingrese el monto del sueldo: '))
      acumulador = acumulador + sueldo
      respuesta = input('Quieres ingresar otro sueldo? Si/No: ')
    else:
      respuesta = 'No'
print('La cantidad total de los sueldos es de:', acumulador)