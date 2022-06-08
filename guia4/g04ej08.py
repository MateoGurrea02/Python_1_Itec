#8) Contar la cantidad de letras (no incluir los separadores).

texto = 'Quiero comer manzanas, solamente manzanas'
contador = 0

for i in range(len(texto)):
  if texto[i] != ' ' and texto[i] != ',':
    contador += 1
print(contador)