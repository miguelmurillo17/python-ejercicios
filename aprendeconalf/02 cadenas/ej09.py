# Escribir un programa que pregunte al usuario la fecha de su nacimiento en 
# formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día o el mes 
# se introduzcan con un solo carácter.

fecha_nacimiento = input('Introduzca su fecha de nacimiento: ')
fecha_descompuesta = fecha_nacimiento.split('/')
print('Día: ' + fecha_descompuesta[0])
print('Mes: ' + fecha_descompuesta[1])
print('Año: ' + fecha_descompuesta[2])