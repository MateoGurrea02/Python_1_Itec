# 3. Primer for: Almacenar en dos listas paralelas, nombres y sexos de 8 personas. 
# Segundo for: Recorrerlas y guardar los nombres de las mujeres en una nueva lista. 
# Mostrar los elementos de la lista resultante.

listaNombre = []
listaSexo = []
listaMujeres = []

for i in range(8):
  nombre = input('Ingrese un nombre: ')
  sexo = input('Ingrese el sexo: ')
  listaNombre.append(nombre)
  listaSexo.append(sexo)

for i in range(8):
  if listaSexo[i] == 'femenino':
    listaMujeres.append(listaNombre[i])

print(listaMujeres)