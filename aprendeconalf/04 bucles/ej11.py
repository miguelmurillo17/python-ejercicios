# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
# una a una las letras de la palabra introducida empezando por la última.
palabra = input('Palabra: ')
print(palabra[::-1])
for i in range(len(palabra)):
    print(palabra[len(palabra)-1-i:len(palabra)-i])
