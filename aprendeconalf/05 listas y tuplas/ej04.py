# Escribir un programa que pregunte al usuario los nÃºmeros ganadores de la 
# loterÃ­a primitiva, los almacene en una lista y los muestre por pantalla 
# ordenados de menor a mayor.
numeros_loteria = []
leer = 'si'
while leer=='si':
    numeros_loteria.append(input('Numero: '))
    leer = input('Leer otro? ')
print(numeros_loteria)
numeros_loteria.sort()
print(numeros_loteria)