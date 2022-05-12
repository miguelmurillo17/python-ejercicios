# Escribir un programa que pida al usuario una palabra y 
# muestre por pantalla si es un palíndromo.

palabra = input('Palabra: ')
palabra_inversa = palabra
palabra = list(palabra)
palabra_inversa = list(palabra_inversa)
palabra_inversa.reverse()

if palabra == palabra_inversa:
    print('Es palindromo')
else:
    print('No es palindromo')
