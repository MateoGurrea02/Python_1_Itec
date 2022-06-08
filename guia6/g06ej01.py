def contarLetras(texto, letra):
  c = 0
  for i in range(len(texto)):
    if texto[i] == letra:
      c += 1
  return c

texto = input("Ingrese un texto: ")
letra = input("Ingrese una letra: ")
cantidad = contarLetras(texto,letra)
print("La letra", letra, "se repite", cantidad, "veces en el texto:", texto)
