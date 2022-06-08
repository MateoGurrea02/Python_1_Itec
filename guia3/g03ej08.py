# 8. Cargar una lista con números. Invertir los elementos sin usar otra lista. 
res = 'si'
listaNumeros = []
while res == 'si':
    numero = int(input('ingrese un numero: '))
    listaNumeros.append(numero)
    res = input('Quiere ingresar otro numero?si/no')

for i in range(len(listaNumeros)):
    listaNumeros[i] = listaNumeros[i] * -1 
print(listaNumeros)
