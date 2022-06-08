# 2. Cargar letras en una lista (while). Contar las vocales (for). Mostrar el total.

listaLetras = []
respuesta = 'si'
contador = 0

while respuesta == 'si':
  letra = input('ingrese una letra: ')
  listaLetras.append(letra)
  respuesta = input('agresgas mas listaLetras? si/no')

for i in range (len(listaLetras)):
  if listaLetras[i] in 'aeiou':
    contador = contador + 1

print('El total de vocales es:', contador)
