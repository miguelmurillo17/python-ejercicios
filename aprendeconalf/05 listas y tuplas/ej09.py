# Escribir un programa que pida al usuario una palabra y muestre por pantalla 
# el número de veces que contiene cada vocal.

vocales=['a','e','i','o','u']
repeticiones = []
palabra = input('Palabra: ')
for vocal in vocales:
    contador = 0
    contador = palabra.count(vocal)
    repeticiones.append(contador)
print(repeticiones)
