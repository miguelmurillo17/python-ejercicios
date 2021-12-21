# Escribir un programa que pregunte el nombre del usuario en la consola 
# y despuÃ©s de que el usuario lo introduzca muestre por pantalla <NOMBRE> 
# tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayÃºsculas y 
# <n> es el nÃºmero de letras que tienen el nombre.
nombre = input('Cual es su nombre completo?: ')
nombreSinEspacios = nombre.replace(' ','')
print('Su nombre tiene',len(nombre),'caracteres')
print('Su nombre tiene',len(nombreSinEspacios),'letras')
