def cadenaLimitada(mensaje="",max=99999999999999,min=0):
    verdadero = False
    while not verdadero:
        c = input(mensaje)
        if len(c) > int(min) and len(c) < int(max):
            verdadero = True
            return c
        else:
            print('La cadena debe tener', min,'caracteres como minimo y',max,'como maximo')
    return c
    
if __name__ == "__main__":
    print(cadenaLimitada('ingrese una cadena: ', max=12,min=4))