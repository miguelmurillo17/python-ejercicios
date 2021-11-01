def SumarRestar(num1,num2):
    suma = num1 + num2
    resta = num1 - num2
    return suma, resta

numero1 = int(input('Introduce numero 1: '))
numero2 = int(input('Introduce numero 2: '))
suma, resta = SumarRestar(numero1,numero2)
print('La suma es: ', suma)
print('La resta es: ', resta)
