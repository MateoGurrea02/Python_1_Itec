# Pedir un nombre y una opción ('>' o '<') y según esta mostrar por ejemplo.: Juan es menor de edad
nombre = input("Ingresa tu nombre:")
opcion = input("Elija un signo < o >:")

if opcion == '<':
    print(nombre, 'Es menor de edad')
else:
    print(nombre, 'Es mayor de edad')