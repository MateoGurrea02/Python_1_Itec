#1) Mostrar por pantalla una lista de 10 números enteros consecutivos, comenzando con un número ingresado por teclado.

numero = int(input("Ingrese un número: "))
for i in range(10):
    print(numero + i)