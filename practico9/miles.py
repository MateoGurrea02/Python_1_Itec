# Se debe realizar el juego MILES.

# Este juego consiste en adivinar un número de 4 cifras que piensa la computadora.
# Dicho número no puede tener cifras repetidas y debe ser superior a 1000 (no puede comenzar con cero).

# El jugador va proponiendo números y el programa le contesta los aciertos:

# Si un dígito del usuario está en el número de la computadora la respuesta será:
# BIEN, si está en la misma posición
# REGULAR si está presente pero en otra posición

# Se termina al adivinar el número exacto y se debe almacenar en un archivo de texto el nombre del jugador y la cantidad de intentos que le llevó ganar.

# El programa también debe permitir mostrar el top ten del ranking de jugadores, ordenados por las sesiones con menor cantidad de intentos para el acierto.
import os
import random

nombres = []
intentosLista = []
listaOrd=[]
def numeroRandom():
  lista = [0,1,2,3,4,5,6,7,8,9]
  lista = random.sample(lista, 4)
  while lista[0] == 0:
    lista = [0,1,2,3,4,5,6,7,8,9]
    lista = random.sample(lista, 4)
  numero = f"{lista[0]}{lista[1]}{lista[2]}{lista[3]}"
  print(numero)
  return numero

def juego(numeroRandom):
  nombreJugador = input("Ingresa tu nombre: ")
  resBien = 0
  intentos = 0
  while resBien != 4:
    numeroElegido = input("Numero -->")
    resRegular = 0
    resBien = 0
    for i in range(len(numeroElegido)):
      if numeroElegido[i] in numeroRandom:
        resRegular += 1
      if numeroElegido[i] == numeroRandom[i]:
        resBien += 1  
        resRegular -= 1
    print("En el numero elegido hay", resBien,"Bien y", resRegular,"Regular")
    intentos += 1
  return nombreJugador,intentos

def jugar():
  print("Escribir un numero de 4 cifras: \n(Recorda que las cifras del numero no se pueden repetir)")
  nombre, intentos = juego(numeroRandom())
  # Si ya existen 10 jugadores y la cantidad de intentos es menor a la persona con mas intentos en la lista, se borra esa persona
  if len(nombres) == 10 and intentos < max(intentosLista):
    maximo = intentosLista.index(max(intentosLista))
    del nombres[maximo]
    del intentosLista[maximo]
  nombres.append(nombre)
  intentosLista.append(intentos)
  input("Presione Enter para volver al Menú")
  
  

def salir():
  pass

def tabla():
  createCsv = open("ranking.csv", "w", encoding="utf-8")
  createCsv.write("Nombre,Intentos\n")
  for i in range(len(nombres)):
    createCsv.write(f"{nombres[i]},{intentosLista[i]}\n")
  createCsv.close()
  input("Se genero un archivo CSV con el top de mejores jugadores con el nombre ranking.csv")


def menu():
    op = ""
    while op != "0":
        os.system("cls")
        print("Menú de Opciones\n")
        print("1) Jugar")
        print("2) Tabla de posiciones")
        print("0) Salir")
        op = input("Ingrese una opción: ")
        match op:
            case "1": jugar()
            case "2": tabla()
            case "3": salir()
menu()
    