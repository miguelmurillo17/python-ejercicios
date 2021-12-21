# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input('Frase: ')
letra_buscada = input('Letra buscada: ')
contador = 0
for letra in frase:
    if letra == letra_buscada:
        contador += 1
print('La letra "{letra}" aparece {contador} veces en "{frase}"'.format(letra=letra,contador=contador,frase=frase))
