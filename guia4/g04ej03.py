frase = input('ingrese una frase cualquiera: ')
letraBuscada = input('ingrese la letra a buscar en la frase: ')
contador = 0

for i in range(len(frase)):
  if frase[i] == letraBuscada:
    contador += 1

print(contador)