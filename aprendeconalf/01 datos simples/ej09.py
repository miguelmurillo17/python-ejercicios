# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión.

cantidad = float(input('Cuánto desea invertir?: '))
interesAnual = float(input('Cuánto es el interes anual?: '))
anios = int(input('Durante cuántos años?: '))
pago = 0
for i in range(anios):
    cantidad = cantidad * interesAnual
print('Obtendrá: $',round(cantidad,2))
