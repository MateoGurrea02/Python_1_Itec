def reemplazarPalabra(frase, palabraNueva, palabraVieja):
    while palabraVieja in frase:
        posPalabraVieja = frase.find(palabraVieja)
        if posPalabraVieja != -1:
            inicio = frase[:posPalabraVieja]
            final = frase[posPalabraVieja + len(palabraVieja):]
            frase = inicio + palabraNueva + final
    return frase

frase = "quiero comer manzanas, solamente manzanas."
palabraVieja = "manzanas"
palabraNueva = "peras"

print(reemplazarPalabra(frase, palabraNueva,palabraVieja))


