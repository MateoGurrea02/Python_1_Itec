# Determinar cuál es la vocal que aparece con mayor frecuencia.

texto = 'Quiero comer manzanas, solamente manzanas'
a = 0
e = 0
i = 0 
o = 0
u = 0
letra = ""

for x in range(len(texto)):
  if texto[x] == 'a':
    a += 1
    letra="A"
  elif texto[x] == 'e':
    e += 1
    letra="E"
  elif texto[x] == 'i':
    i += 1
    letra="I"
  elif texto[x] == 'o':
    o += 1
    letra="O"
  elif texto[x] == 'u':
    u += 1
    letra="U"

print(letra,max(a,e,i,o,u))



