# Escribir un programa que pregunte el nombre del usuario en la consola y
# un número entero e imprima por pantalla en líneas distintas el nombre 
# del usuario tantas veces como el número introducido.

nombre = input('Cuál es su nombre?: ')
repeticiones = int(input('Introduzca un entero: '))
for i in range(1,repeticiones+1):
    print(nombre)
