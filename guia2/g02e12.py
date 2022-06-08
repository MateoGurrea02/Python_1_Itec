# 12)Pedir nombres y sexo de personas y mostrar el total de mujeres y el nombre de cada una.

respuesta = 'Si'
lista = ''
contador = 0

while respuesta == 'Si':
  nombre = input('Ingrese un nombre: ')
  sexo = input('Ingrese el sexo de la persona: ')
  if sexo == 'mujer':
    contador += 1
    lista = lista + nombre + '; '
    respuesta = input('Quiere ingresar otra persona: ')
  else:
    respuesta = input('Quiere ingresar otra persona: ')

  
print('La cantidad de mujeres totales son:',contador,'y los nombres son:', lista)