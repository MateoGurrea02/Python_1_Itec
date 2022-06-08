#6) Buscar una palabra completa en un texto y contar cuántas veces está

texto = 'Quiero comer manzanas, solamente manzanas'
palabraBuscada = input('ingrese una palabra a buscar: ')
texto = texto.replace(',','').split(' ')
contador = 0
for i in range(len(texto)):
    if texto[i] in palabraBuscada:
        contador = contador + 1

print(contador)        