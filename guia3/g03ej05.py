# 5. Guardar en una lista los números pares mayores que 0 y menores que 31. 
res = 'si'
numberList = []

while res == 'si':
    number = int(input('ingrese un numero: '))
    if number > 0 and number < 31 and number % 2 == 0: 
        numberList.append(number)
    res = input('quieres ingresar otro numero: ')    

print(numberList)