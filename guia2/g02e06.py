# 6)Preguntar cuántas personas se van a cargar y luego solicitar sus edades, mostrando al final la edad promedio.

pregunta = int(input('Cuantas personas quiere cargar? '))
acumulador = 0

for i in range(pregunta):
  edad = int(input('Ingrese una de las edades:'))
  acumulador = acumulador + edad

promedio = acumulador / pregunta

print('El promedio de las edades es de:', promedio)