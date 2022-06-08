def concatenar(*args,caracter=' '):
    cadena = ''
    for i in range(len(args)):
        cadena = cadena + args[i] + caracter
    return cadena

if __name__ == "__main__":
    print(concatenar('hola','como','estas','ss',' '))