# Escribir un programa que pregunte por consola el precio de un producto en euros 
# con dos decimales y muestre por pantalla el número de euros y el número de céntimos 
# del precio introducido.

precio = float(input('Introduzca el precio del producto: '))
precioString = str(precio)
print(precioString[:precioString.find('.')],' pesos y ',precioString[precioString.find('.')+1:len(precioString)],' centavos')
