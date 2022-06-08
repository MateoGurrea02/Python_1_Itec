# 10. Ingresar la lluvia caída en milímetros para cada día de la semana. 
# Mostrar al final el total de lluvia caída y el nombre del día que más llovió. 

dias = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
lluvia = [10, 5, 6, 30, 3, 0, 25]
llovioMas = 0
diaNombreLlovioMas = ''
acumulador = 0
for i in range(7):
    if lluvia[i] > llovioMas:
        llovioMas = lluvia[i]
        diaNombreLlovioMas = dias[i]
    acumulador = acumulador + lluvia[i]

print('El total de mm que llovio en el semana es:', acumulador, 'y el dia', diaNombreLlovioMas, 'y llovio', llovioMas)
    