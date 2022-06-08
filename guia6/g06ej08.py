def carga():
  nombres = []
  for i in range(6):
    nombre = input('Nombre: ')
    nombres.append(nombre)
  return nombres

def nombrePorPosicion(nombres):
  nombre = input('Nombre a buscar: ')
  for i in range(len(nombres)):
    if nombres[i] in nombre:
      return i,nombre

posicion, nombre = nombrePorPosicion(carga())
print('El nombre:', nombre)
print('esta en la posicion:',posicion)
