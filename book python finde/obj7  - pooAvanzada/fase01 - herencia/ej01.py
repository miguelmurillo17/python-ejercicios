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
lavadora1.MostrarLavadora()
lavadora2.MostrarLavadora()
