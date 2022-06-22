# 8) funciones que reciban una cantidad indeterminada de objetos y devuelvan:
#   a)El total acumulado (14)
#   b)El objeto que tiene más y su cantidad (manzanas - 9)
# Por ejemplo con estos datos: 3 bananas, 9 manzanas y 2 frutillas

def totalAcumulado(**kwargs):
  acumulador = 0
  for i in kwargs.values():
    acumulador += i
  return acumulador

def hayMas(**kwargs):
  cantidad = 0
  nombreMayor = ''
  for k,i in kwargs.items():
    if i >= cantidad:
      cantidad = i
      nombreMayor = k
  return nombreMayor, cantidad
  
nombre,cantidad =  hayMas(manzanas=3,peras=5,naranja=1)

print(f"El total acumulado {totalAcumulado(manzanas=3,peras=4)} ")
print(f"El objeto que tiene mas y su cantidad ({nombre} - {cantidad})")