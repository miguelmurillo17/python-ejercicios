# Escribir un programa que pida al usuario un número entero positivo y muestre por 
# pantalla todos los números impares desde 1 hasta ese número separados por comas.
numero = int(input('numero: '))
print('Impares conenidos:')
for i in range(numero):
    numero_evaluado = i+1
    if (numero_evaluado%2 == 0):
        print(numero_evaluado)