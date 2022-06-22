# 10. Cargar una lista con números. Invertir los elementos (sin usar reverse). Mostrar.

def reverseList(lista):
  actualNum = 0
  for i in range(round(len(lista)/ 2)):
    if i == 0:
      actualNum = lista[i]
      lista[i] = lista[i - 1]
      lista[i - 1] = actualNum
    else:
      actualNum = lista[i]
      lista[i] = lista[i * -1 -1]
      lista[i * -1 -1] = actualNum
  return lista

lista = [1,2,3,4,5,6,23,12,5,4,0]
print(reverseList(lista))