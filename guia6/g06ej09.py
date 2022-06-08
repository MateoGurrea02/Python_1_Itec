numeros = [10,8,9]

def promedio(numeros):
  suma = 0
  for i in range(len(numeros)):
    suma = suma + numeros[i]
  resultado = suma / len(numeros)
  return resultado

def mayorQue(promedio,numeros):
  numerosMayores = []
  for i in range(len(numeros)):
    if numeros[i] > promedio:
      numerosMayores.append(numeros[i])
  return numerosMayores, promedio

numerosMayores, numeroPromedio = mayorQue(promedio(numeros),numeros)
print('El promedio es:',numeroPromedio, 'y los numeros mayores al promedio son:', numerosMayores)