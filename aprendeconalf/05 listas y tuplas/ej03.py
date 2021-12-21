# Escribir un programa que almacene las asignaturas de un curso en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre 
# por pantalla con el mensaje En <asignatura> has sacado <nota> 
# donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una 
# de las correspondientes notas introducidas por el usuario.

materias = ['matematicas','fisica','quimica','historia','lengua']
calificaciones = []
for materia in materias:
    calificacion = float(input('Cuánto sacó en {materia}? '.format(materia=materia)))
    calificaciones.append(calificacion)
for i in range(len(materias)):
    print('En "',materias[i],'" sacó: ',calificaciones[i])
