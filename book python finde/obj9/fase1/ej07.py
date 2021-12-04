print('Inicio de la ejecucion del programa')
try:
    print(3/0)
except ZeroDivisionError:
    print('ERROR: Divison entre cero')
except:
    print('ERROR: Ha ocurrido un error inesperado')
else:
    print('No se ha producido error')
finally:
    print('Fin de la ejecucion del programa')
