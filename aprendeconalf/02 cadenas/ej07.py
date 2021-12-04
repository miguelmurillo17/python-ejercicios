# Escribir un programa que pregunte el correo electrónico del usuario en la consola 
# y muestre por pantalla otro correo electrónico con el mismo nombre 
# (la parte delante de la arroba @) pero con dominio ceu.es.

#opcion 1:
correo = input('Ingrese su email: ')
correoNuevo = ''
posicion = len(correo)
for i in range(len(correo)):
    if correo[i:i+1] == '@':
        posicion = i
correoNuevo = correo[0:posicion] + '@ceu.es'
print(correoNuevo)
#opcion 2
print('')
email = input('Ingrese su email: ')
print(email[:email.find('@')]+ '@ceu.es')