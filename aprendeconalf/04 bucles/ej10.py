# Escribir un programa que pida al usuario un número entero y muestre por pantalla 
# si es un número primo o no.

numero = int(input('Número: '))
descripcion_numero = 'Si es primo'
for i in range(numero-1,1,-1):
    residuo = numero%i
    if residuo==0:
        descripcion_numero = 'No es primo'
        exit
print(descripcion_numero)