# 1. Pedir el ingreso de 10 números. Contar los mayores de 23 y almacenar los que cumplen la condición.  Mostrar la cantidad y los números guardados.

lista = []
for i in range(10):
  numeros = int(input('ingresa 1 numero'))
  if numeros > 23:
    lista.append(numeros)

print('la cantidad de numeros mayores a 23 es:', len(lista), 'y son:', lista)  