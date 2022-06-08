# Calcular el sueldo a cobrar teniendo en cuenta que  los empleados que no han faltado y  cuya antigüedad es superior a 5 años, tienen un adicional del 30% sobre el sueldo básico ($47.000). 
# Pedir la cantidad de días no trabajados y año de ingreso en la empresa.

sueldoBasico = 47000
diasNoTrabajados = int(input('Ingrese la cantidad de dias que no trabajo:'))
anioIngreso = int(input('Ingrese el año de ingreso a la empresa:'))
adicional = sueldoBasico + (sueldoBasico * ( 30 / 100))

antiguedad = 2022 - anioIngreso

if (diasNoTrabajados <= 1 and antiguedad >= 5):
    print('A usted le corresponden', adicional, 'de sueldo')
else:
    print('A usted le corresponden', sueldoBasico, 'de sueldo')