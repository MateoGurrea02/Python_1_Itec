
def carga():
    nombres = []
    sexos = []
    for i in range(3):
        nombre = input('Nombre: ')
        sexo = input('Sexo: ')
        nombres.append(nombre)
        sexos.append(sexo)
    return nombres, sexos

def mostrarMujeres(nombres, sexos):
    for i in range(len(sexos)):
        if sexos[i] == 'f':
            print(nombres[i])

ns, ss = carga()
mostrarMujeres(ns, ss)