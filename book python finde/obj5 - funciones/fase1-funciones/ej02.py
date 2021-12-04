def EsMayorQueCero(num):
    resultado = ''
    if num > 0:
        resultado = 'Es mayor que cero'
    else:
        resultado = 'No es mayor que cero'
    return resultado

numero = int(input('Introduce un numero: '))
resultado_evaluar = EsMayorQueCero(numero)
print(resultado_evaluar)