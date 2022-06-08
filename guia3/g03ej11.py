# 11. Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad.

import re


mayoresDe18 = []
nombres = []
fechas = []
res = 'si'     
dA = 3
mA = 5
aA = 2022


while res == 'si':
  diaMesAnio = []
  nombre = input('Ingresa un nombre: ')
  dN = int(input('ingresa el dia de nacimiento'))
  mN = int(input('ingresa el mes de nacimiento'))
  aN = int(input('ingresa el año de nacimiento'))
  diaMesAnio.append(dN)
  diaMesAnio.append(mN)
  diaMesAnio.append(aN)
  fechas.append(diaMesAnio)
  nombres.append(nombre)
  res = input('Quieres escribir otro nombre?')

for i in range(len(nombres)):
  edad = aA - fechas[i][2]
  if(fechas[i][1] > mA) or(fechas[i][1] == mA and fechas[i][0] > dA):
    edad = edad - 1
  if edad > 18:
    mayoresDe18.append(nombres[i])

print(mayoresDe18)