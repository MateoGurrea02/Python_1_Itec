# 4. Dada una lista con números, crear otra con los cuadrados de esos valores. 

res = 'si'
listaNumeros = []
listaCuadrados = []
while res == 'si':
  numero = int(input('Ingresa un numero'))
  listaNumeros.append(numero)
  res = input('Quieres agregar otro numero?si/no ')

for i in range(len(listaNumeros)):
  cuadrado = listaNumeros[i] * listaNumeros[i]
  listaCuadrados.append(cuadrado)

print(listaNumeros)
print(listaCuadrados)  
