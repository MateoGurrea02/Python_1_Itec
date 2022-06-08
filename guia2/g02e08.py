# 8)Ingresar autos y sus precios y contar cuantos valen entre $1.460.000 y $2.850.000. Terminar la carga cuando el valor ingresado sea 0.

precio = 1
acumulador = 0

while precio != 0:
  automovil = input('Nombre del auto: ')
  precio = int(input('Ingrese el precio del auto: '))
  
  if precio >= 1460000 and precio <= 2850000:
    acumulador = acumulador + 1
  else:
    pass

print('La cantidad de autos que valen entre $1.460.000 y $2.850.000 son', acumulador)