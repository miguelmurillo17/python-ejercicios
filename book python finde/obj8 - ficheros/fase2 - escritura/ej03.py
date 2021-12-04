print('\n')
print('*** Fichero original:')
fmodificar = open(r'obj8 - ficheros\fase2 - escritura\prueba_creada.txt','w')
fmodificar.write('Nuevo texto :D')
fmodificar.close()

fleer = open(r'obj8 - ficheros\fase2 - escritura\prueba_creada.txt','r')
print(fleer.read())
fleer.close()
