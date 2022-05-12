# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista 
# las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las 
# asignaturas que el usuario tiene que repetir

materias = ['matematicas','fisica','quimica','historia','lengua']
leer = 'si'
while leer=='si':
    materia_aprobada = input('Materia aprobada: ')
    materias.remove(materia_aprobada)
    leer = input('Leer otro? ')
print('Debe cursar:')
for materia in materias:
    print(materia,end=', ')
