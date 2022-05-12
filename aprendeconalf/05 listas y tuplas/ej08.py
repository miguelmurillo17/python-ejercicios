# Escribir un programa que pida al usuario una palabra y 
# muestre por pantalla si es un palíndromo.

palabra = input('Palabra: ')
letras_palabra = list(palabra)
print(letras_palabra)
palindromo = True
for i in range(len(letras_palabra)):
    print(letras_palabra[i])
    print(letras_palabra[len(letras_palabra)-i-1])
    print('*')
    if letras_palabra[i] != letras_palabra[len(letras_palabra)-i-1]:
        palindromo = False
        break
if palindromo:
    print('Es palindromo')
else:
    print('No es palindromo')
