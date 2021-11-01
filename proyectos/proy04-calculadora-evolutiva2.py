import os

def SolicitarNumeros(textoMostrar):
    print(textoMostrar)
    n1 = int(input('Ingrese numero 1: '))
    n2 = int(input('Ingrese numero 2: '))

def LeerNumero(descripcionNumero):
    correcto = False
    while correcto == False:
        try:
            numero = int(input('Ingrese ' + descripcionNumero))

def Sumar(n1,n2):
    print('Resultado: ',n1 + n2)

def Restar(n1,n2):
    print('Resultado: ',n1 - n2)

def Multiplicar(n1,n2):
    print('Resultado: ',n1 * n2)

def Dividir(n1,n2):
    print('Resultado: ',n1 / n2)

def Calculadora():
    continuar = True
    while continuar:
        resultado = 0
        os.system ("cls")
        print('''
        CALCULADORA

        Menu:
        1.- Sumar
        2.- Restar
        3.- Multiplicar
        4.- Dividir
        5.- Salir

        ''')
        opcion = int(input('Seleccione una opcion: '))

        if opcion == 5:
            continuar = False
        elif opcion > 0 and opcion < 5:
            n1 = int(input('Ingrese numero 1: '))
            n2 = int(input('Ingrese numero 2: '))
            if opcion == 1:
                Sumar(n1,n2)
            elif opcion == 2:
                Restar(n1,n2)
            elif opcion == 3:
                Multiplicar(n1,n2)
            elif opcion == 4:
                Dividir(n1,n2)
            input('')
        else:
            print('Favor de ingresar una opcion valida')
            input('')

Calculadora()