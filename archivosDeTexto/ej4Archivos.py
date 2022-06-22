# Tenemos un archivo deudores.txt con información de personas que adeudan dinero.

# Necesitamos saber el nombre, la dirección de correo y el saldo de todos los que deben más de doscientos mil pesos y cuya deuda sea del año pasado.

# Hacer:
# Recorrer el archivo deudores.txt y grabar uno nuevo llamado morosos.txt con los datos requeridos. 
# Para los saldos, el nuevo archivo NO tiene que tener el signo pesos ($) ni los centavos.
# El nuevo archivo tiene que tener cabecera en la primera línea con los nombres de los datos, similar al archivo deudores.txt.

a = open("deudores.txt", "r", encoding="utf-8")
listaPersonas = a.readlines()

def formatoArchivo(archivo):
  idsDeudores = []
  nombresDeudores = []
  correosDeudores = []
  saldosDeudores = []
  for i in range(len(archivo)):
    if i == 0:
      pass
    else:
      personas = archivo[i].split(',')
      saldo = int(personas[4].split('.')[0].split('$')[1])
      anio = int(personas[5].split('/')[2])
      print(saldo)
      print(anio)
      if saldo > 200000 and anio < 2020:
        idsDeudores.append(personas[0])
        nombresDeudores.append(personas[1])
        correosDeudores.append(personas[2])
        saldosDeudores.append(saldo)
  return idsDeudores, nombresDeudores, correosDeudores, saldosDeudores

def crearArchivo(ids, nombres, correos, saldos, nombreArchivo):
  a = open(f"{nombreArchivo}.txt", "w", encoding="utf-8")
  a.write("id,nombre,correo,saldo\n")
  for i in range(len(ids)):
    a.write(f"{ids[i]},{nombres[i]},{correos[i]},{saldos[i]}\n")
  a.close()

idsDeudores, nombresDeudores, correosDeudores, saldosDeudores = formatoArchivo(listaPersonas)
crearArchivo(idsDeudores, nombresDeudores, correosDeudores, saldosDeudores, 'morosos')
    


