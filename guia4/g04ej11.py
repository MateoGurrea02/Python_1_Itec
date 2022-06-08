# 11 Averiguar qué cantidad de letras tiene la palabra más larga y cual es.

texto = "Quiero comer manzanas, solamente manzanas."
texto = texto.replace(',','').split(' ')
palabraLarga = ''
for i in range(len(texto)):
  if len(texto[i]) > len(palabraLarga):
    palabraLarga = texto[i]

print(palabraLarga)