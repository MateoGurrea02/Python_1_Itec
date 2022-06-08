# 12. Pedir nombres y sexo de personas y mostrar al final el total de mujeres y el nombre de cada una.
res = 'si'
nombres = []
sexos = []
mujeres = []

while res == 'si':
  nombre = input('Ingrese un nombre: ')
  sexo = input('Ingrese el sexo de la persona: ')
  nombres.append(nombre)
  sexos.append(sexo)
  res = input('Quieres ingresar otro nombre?: ')

for i in range(len(sexos)):
  if sexos[i] == 'mujer':
    mujeres.append(nombres[i])


print('La cantidad de mujeres totales son:', len(mujeres),'y los nombres son:', mujeres)