# Una panadería vende barras de pan a $3.49 cada una. 
# El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de 
# barras vendidas que no son del día. Después el programa 
# debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.

precio_pan_del_dia = 3.49
precio_pan_viejo = precio_pan_del_dia * 0.6

cantidad_pan_viejo_vendido = int(input('Cuántos panes viejos se vendieron?: '))
print('Precio habitual de una barra de pan:  $',precio_pan_del_dia)
print('Descuento que se le hace por no ser fresca: $',round(precio_pan_del_dia-precio_pan_viejo,2))
print('Coste final total: $',round(cantidad_pan_viejo_vendido*precio_pan_viejo,2))