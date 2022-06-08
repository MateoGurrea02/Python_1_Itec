#  Mostrar el valor doble del número de dos cifras (que es el único número) encontrado en la cadena. 
# Ej.: 'Juan tiene 25 años' mostraría el número 50, ‘El dólar va a llegar este mes a 57 pesos casi seguro’,  mostraría 114.

texto = 'Juan tiene 25 años'
numero = ''
for i in range(len(texto)):
  if texto[i] in '1234567890':
    numero = numero + texto[i]
doble = int(numero) * 2
print(doble)