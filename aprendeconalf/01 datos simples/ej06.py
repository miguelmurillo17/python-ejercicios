peso = float(input('Ingrese su peso (en kilos): '))
estatura = float(input('Ingrese su estatura (en metros): '))
imc = peso / (estatura**2)
resultado = 'Su IMC es ' + str(imc)
print(resultado)
#redondear
resultado = 'Su IMC es ' + str(round(imc,2))
print(resultado)