def inputNumber(tipoDeDato, cartel):
  validado = False
  while not validado:
    n = input(cartel)
    try:
      if tipoDeDato == 'entero':
        n = int(n)
      elif tipoDeDato == 'real':
        n = float(n)
      validado = True
    except:
      print('no es un ', tipoDeDato)
  return n

if __name__ == "__main__":
  altura = inputNumber('real','Ingrese su altura')
  numero1 = inputNumber('entero','Ingrese un numero')