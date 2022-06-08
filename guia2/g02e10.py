# 10)Dada una lista de nombres y de salarios respectivos, 
# determinar el salario mínimo y mostrar el nombre de la persona que menos gana.
respuesta = 'Si'
salarioAntiguo = 10000000000000000000
while respuesta == 'Si':
  nombre = input('Ingrese un nombre: ')
  salario = int(input('Ingrese el salario: '))
  if salario < salarioAntiguo:
    salarioAntiguo = salario
    nombreAntiguo = nombre
    respuesta = input('Quiere ingresar otra persona: ')
  else:
    respuesta = input('Quiere ingresar otra persona: ')

  
print('El salario mas bajo es el de:', nombreAntiguo, 'y cobra', salarioAntiguo)