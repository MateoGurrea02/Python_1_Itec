# 7. Dada una lista cargada con 7 números enteros, obtener el promedio. 
# Mostrar por pantalla dicho promedio y los números de la lista que sean mayores que él.

listaNumeros = [10,5,9,2,4,7,10]
acumulador = 0
nMayoresPromedio = []
for i in range(7):
    acumulador = acumulador + listaNumeros[i]

promedio = acumulador / len(listaNumeros)

for i in range(7):
    if promedio < listaNumeros[i]:
        nMayoresPromedio.append(listaNumeros[i])

print('el promedio es', promedio,'y los numeros mayor al promedio son:',nMayoresPromedio)
