# Escribir un programa que pregunte el nombre el un producto, su precio y 
# un número de unidades y muestre por pantalla una cadena con el nombre del 
# producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
# el número de unidades con tres dígitos y el coste total con 8 dígitos enteros 
# y 2 decimales.

producto = input('Producto: ')
precio_unitario = float(input('Precio unitario: '))
unidades = int(input('Unidades: '))

print('{producto}, Costo unitario: ${precio_unitario:6.2f}, por {unidades:3d} unidades, es un total de ${total:8.2f}'.format(producto=producto, precio_unitario=precio_unitario, unidades=unidades, total=unidades*precio_unitario))