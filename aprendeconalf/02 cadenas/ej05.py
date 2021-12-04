# Escribir un programa que pida al usuario que introduzca una frase 
# en la consola y muestre por pantalla la frase invertida.

frase = input('Ingrese una frase: ')
fraseInvertida = ''
for i in range(len(frase)):
    fraseInvertida = fraseInvertida + frase[len(frase)-1-i:len(frase)-i]
print(fraseInvertida)
print(frase[::-1])

#Slicing:
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1

# One way to remember how slices work is to think of the indices as pointing 
# between characters, with the left edge of the first character numbered 0. 
# Then the right edge of the last character of a string of n characters has index n.