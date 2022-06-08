"""
Validar un número (reutilizar inputInt/inputFloat o bien inputNumber 
si usan una sola función para validar ambos tipos de datos). 
Debe tener un rango opcional.
Opciones de uso:
n = inputNumber('Ingrese un entero', 3, 7)
m = inputNumber('Cualquier entero: ')
maxito = inputNumber('ingrese un entero', max=999)
minito = inputNumber('ingrese un entero', min=1001)
"""
from input_number import inputNumber
print(inputNumber('entero','ingrese un entero'))