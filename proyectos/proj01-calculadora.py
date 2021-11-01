import os

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
        num1 = int(input('Ingrese numero 1: '))
        num2 = int(input('Ingrese numero 2: '))
        if opcion == 1:
            resultado = num1 + num2
        elif opcion == 2:
            resultado = num1 - num2
        elif opcion == 3:
            resultado = num1 * num2
        elif opcion == 4:
            resultado = num1 / num2
        print('El resultado es: ', resultado)
        input('')
    else:
        print('Favor de ingresar una opcion valida')
        input('')