print('\n')
print('*** Fichero original:')
fcrear = open(r'obj8 - ficheros\fase2 - escritura\prueba_creada.txt','x')
fcrear.write('Este es el titulo\n')
fcrear.write('Esta es la segunda linea\n')
fcrear.close()
fleer = open(r'obj8 - ficheros\fase2 - escritura\prueba_creada.txt','r')
print(fleer.read())
fleer.close()
