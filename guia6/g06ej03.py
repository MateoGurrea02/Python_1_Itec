def contarLetras(frase):
    c = 0 
    for i in range(len(frase)):
        if frase[i] in ' ,.':
            pass
        else:
            c += 1
    return c
print(contarLetras('hola como estas'))