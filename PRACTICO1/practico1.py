# 1) Mostrar los apellidos, luego una coma, luego un espacio y finalmente el nombre de pila de todas las personas.

nombres =['Ana Torres','Kate Hudson','Benicio Quesada','Susana Campoamores','Carlos Santamaría','Azul Skarsgard','Walter Catalejos']
sexos = ['f','f','m','f','m','f','m']
nacimientos = ['02/05/1943','07/09/1984','10/02/1971','21/12/1967','18/07/1959','30/08/1995','30/01/1982']
nombreSeparado = []
edadActual = 0
apellidoMasLargo = '0'
fechas = []
dA = 10
mA = 5
aA = 2022

print('Apellido y nombre de las personas:')
for i in range(len(nombres)):
  # Separacion del los nombres completos con el formato pedido
  nombreSeparado.append(nombres[i].split(' '))
  formatoNombre = nombreSeparado[i][1] + ', ' + nombreSeparado[i][0]
  print(formatoNombre)
  # Encuentra el apellido mas largo para pintarlo mas adelante
  if len(apellidoMasLargo) < len(nombreSeparado[i][1]):
    apellidoMasLargo = nombreSeparado[i][1] 

print('----------------------------------')
# Nombre del  varon mas Viejo
for i in range(len(nombres)):
  fechas.append(nacimientos[i].split('/'))
  if sexos[i] == 'm':
    edad = aA - int(fechas[i][2])
    if(int(fechas[i][1]) > mA) or(int(fechas[i][1]) == mA and int(fechas[i][0]) > dA):
      edad = edad - 1
      if edadActual < edad:
        print('El nombre de pila del varón más viejo es:',nombreSeparado[i][0])

print('----------------------------------')

print('El apellido más largo es:',apellidoMasLargo)