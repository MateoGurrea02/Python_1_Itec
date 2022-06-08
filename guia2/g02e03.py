# 3)Pedir el ingreso de 5 números. Contar los mayores de 23. Mostrar el resultado.
contador = 0
for i in range (5):
  numero = int(input('Ingrese 1 numero: '))
  if numero > 23:
    contador = contador + 1

print(contador)