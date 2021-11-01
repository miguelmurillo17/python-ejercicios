def SumarRestar(num1,num2):
    return Sumar(num1,num2),Restar(num1,num2)

def Sumar(n1,n2):
    return n1 + n2
    
def Restar(n1,n2):
    return n1 - n2


numero1 = int(input('Introduce numero 1: '))
numero2 = int(input('Introduce numero 2: '))
suma, resta = SumarRestar(numero1,numero2)
print('La suma es: ', suma)
print('La resta es: ', resta)
