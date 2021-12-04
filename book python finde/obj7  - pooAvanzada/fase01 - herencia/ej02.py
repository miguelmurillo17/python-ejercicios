class Electrodomestico:
    def __init__(self):
        self.__Encendido = False
        self.__Tension = 0
    def Encender(self):
        self.__Encendido = True
    def Apagar(self):
        self.__Encendido = False
    def Encendido(self):
        return self.__Encendido
    def SetTension(self,tension):
        self.__Tension = tension
    def GetTension(self):
        return self.__Tension

class Lavadora(Electrodomestico):
    def __init__(self):
        self.__RPM = 0
        self.__Kilos = 0
    def SetRPM(self,rpm):
        self.__RPM = rpm
    def SetKilos(self,kilos):
        self.__Kilos = kilos
    def MostrarLavadora(self):
        print('**********')
        print('Lavadora:')
        print('\tRPM: ',self.__RPM)
        print('\tKilos: ',self.__Kilos)
        print('\tTension: ',self.GetTension())
        if self.Encendido():
             print('\tLavadora encendida')
        else:
            print('\tLavadora apagada')
        print('**********')

class Microondas(Electrodomestico):
    def __init__(self):
        self.__PotenciaMAxima = 0
        self.__Grill = 0
    def SetPotenciaMaxima(self,potencia):
        self.__PotenciaMAxima = potencia
    def SetGrill(self,grill):
        self.__Grill = grill
    def MostrarMicroondas(self):
        print('**********')
        print('Microondas:')
        print('\tPotencia maxima: ',self.__PotenciaMAxima)
        print('\tGRill: ',self.__Grill)
        print('\tTension: ',self.GetTension())
        if self.Encendido():
             print('\tMicroondas encendido')
        else:
            print('\tMicroondas apagado')
        print('**********')

lavadora1 = Lavadora()
lavadora1.SetRPM(2000)
lavadora1.SetKilos(20)
lavadora1.SetTension(220)
lavadora1.Encender()
lavadora2 = Lavadora()
lavadora2.SetRPM(2003)
lavadora2.SetKilos(18)
lavadora2.SetTension(110)
lavadora2.Encender()
lavadora2.Apagar()
microondas1 = Microondas()
microondas1.SetPotenciaMaxima(1000)
microondas1.SetGrill(10)
microondas1.SetTension(110)
microondas1.Encender()
microondas1.Apagar()
lavadora1.MostrarLavadora()
lavadora2.MostrarLavadora()
microondas1.MostrarMicroondas()
