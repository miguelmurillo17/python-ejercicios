# sumar dos numeros sin usar el signo de multiplicacion

def multiplicar(n1,n2):
    resultado = 0
    for i in range(n1):
        resultado += n2
    print('Multiplicacion: ',resultado)

#def solicitar_numeros():
#    n1 = int(input('Ingrese numero 1'))
#    n2 = int(input('Ingrese numero 2'))

#solicitar_numeros()
n1 = int(input('Ingrese numero 1: '))
n2 = int(input('Ingrese numero 2: '))
multiplicar(n1,n2)