# Escribir un programa que pregunte por consola por los productos de una 
# cesta de la compra, separados por comas, y muestre por pantalla cada uno 
# de los productos en una línea distinta.

lista_productos = input('Introduzca la lista de productos (separados por coma): ')
productos = lista_productos.split(',')
for producto in productos:
    print(producto)
