def Sumar(*valores):
    suma = 0
    for i in valores:
        suma = suma + i
    return suma

def SumarLista(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

resultado = Sumar(1,2,3,4,5)
print(resultado)

resultado = SumarLista([1,2,3,4,6])
print(resultado)
