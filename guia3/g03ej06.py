# 6. Ingresar nombres en una lista, luego buscar un nombre y de encontrarlo decir en qué posición está.

res = 'si'
listaNombre = []
while res == 'si':
    nombre = input('ingrese un nombre')
    listaNombre.append(nombre)
    res = input('quieres ingresar otro numero: ')

nombreBuscado = input('busque un nombre: ')
 
for i in range(len(listaNombre)):
    if nombreBuscado == listaNombre[i]:
        print('El nombre', nombreBuscado, 'se encuentra en la posicion', i)
