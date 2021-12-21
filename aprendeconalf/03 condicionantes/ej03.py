# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

dividendo = float(input('Introduzca el dividendo:'))
divisor = float(input('Introduzca el divisor:'))

if (divisor==0):
    print('No es posible dividir entre cero')
else:
    cociente = int(dividendo/divisor)
    residuo = int(dividendo%divisor)
    print('El cociente es: {cociente:3.0f} y el residuo es {residuo:3.0f}'.format(cociente=cociente,residuo=residuo))
