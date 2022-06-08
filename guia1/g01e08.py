# Pasar un período expresado en segundos a un período expresado en días, horas, minutos y segundos.
from difflib import restore


totalSegundos = int(input('Inserte cantidad de segundos:'))

dias = totalSegundos // 86400

resto = totalSegundos - (dias * 86400)

horas = resto // 3600

resto = resto -(horas * 3600)

minutos = resto // 60

segundos = resto - (minutos * 60)


print('el total de segundos', totalSegundos, 'es equivalente a',dias, 'dias', horas, 'horas', minutos, 'minutos y', segundos, 'segundos') 