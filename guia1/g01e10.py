# Preguntar nombre, carrera en la que se inscribe y ciudad donde vive un ingresante al Instituto. 
# Los estudiantes de la carrera de Electromecánica y que no viven en Río Cuarto tendrán un 15% de descuento en la cuota que es de $7000. 
# Mostrar nombre, ciudad, carrera y monto final de la cuota.

nombre = input('Ingrese su nombre: ')
carrera = input('Ingrese la carrera en la que desea inscribirse: ')
ciudad = input('Ingrese su ciudad: ')
valorCuota = 7000

if(carrera == 'Electromecanica' and ciudad != 'Rio Cuarto'):
    cuota = valorCuota * .85
    print(nombre, carrera, ciudad, cuota)
else:
    cuota = 7000
    print(nombre, carrera, ciudad, cuota)