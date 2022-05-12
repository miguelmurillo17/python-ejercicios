# Escribir un programa que almacene el abecedario en una lista, elimine de la lista 
# las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista 
# resultante.
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
longitud_inicial = len(abecedario)
for i in range(longitud_inicial,1,-1):
    if i%3==0:
        abecedario.pop(i-1)
print(abecedario)

lista = [1,2,3,4,5]
lista.pop(4)
print(lista)
lista.pop(0)
print(lista)
