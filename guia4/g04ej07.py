# Buscar una palabra y reemplazarla por otra todas las veces que aparezca.
# Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.' Sin usar replace.

from ntpath import join


texto = 'Quiero comer manzanas, solamente manzanas'
palabraBuscada = input('ingrese una palabra a buscar: ')
palabraCambiada =  input('ingrese una palabra a cambiar: ')
texto = texto.replace(',','').split(' ')
for i in range(len(texto)):
    if texto[i] in palabraBuscada:
      texto[i] = palabraCambiada

print(' '.join(texto))  