# Escribir un programa que pida al usuario un número entero y muestre por 
# pantalla un triángulo rectángulo como el de más abajo.

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

numero = int(input('Numero: '))
base = 1
for i in range(numero):
    cadena = ''
    for j in range(base,0,-2):
        cadena = cadena + str(j) + ' '
    print(cadena)
    base = base + 2
