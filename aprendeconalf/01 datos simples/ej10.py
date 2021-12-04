# Una juguetería tiene mucho éxito en dos de sus productos: 
# payasos y muñecas. Suele hacer venta por correo y la empresa
# de logística les cobra por peso de cada paquete así que deben
# calcular el peso de los payasos y muñecas que saldrán en cada
# paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
# Escribir un programa que lea el número de payasos y muñecas 
# vendidos en el último pedido y calcule el peso total del paquete 
# que será enviado.

peso_payaso = 112
peso_munieca = 75
cantidad_payaso = int(input('Cuántos payasos enviará?: '))
cantidad_munieca = int(input('Cuántas muñecas enviará?: '))
peso_total_payasos = peso_payaso * cantidad_payaso
peso_total_muniecas = peso_munieca * cantidad_munieca
peso_total = round((peso_total_muniecas + peso_total_payasos)/1000,2)
print('El envío pesará: ',peso_total,' Kgs.')
