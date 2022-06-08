# 9. Cargar en dos listas paralelas nombres y sueldos. 
# Luego mostrar los nombres de las personas que ganan más de $185000.

nombres = ['Mateo', 'Juan', 'Pepe', 'Ricardo']
sueldos = [186000, 184000, 10000, 200000]
gananMas = []
for i in range(len(sueldos)):
    if sueldos[i] > 185000:
        gananMas.append(nombres[i])        
print('Las personas que ganan mas de 185.000 son:', gananMas)