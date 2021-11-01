class PuntoPublico:
    def __init__(self,x,y):
        self.X = x
        self.Y = y

class PuntoPrivado:
    def __init__(self,x,y):
        self.__X = x
        self.__Y = y
    def GetX(self):
        return self.__X
    def GetY(self):
        return self.__Y
    def SetX(self,x):
        self.__X = x
    def SetY(self,y):
        self.__Y = y

puntoPublico = PuntoPublico(1,2)
puntoPrivado = PuntoPrivado(3,4)
print('Punto publico: ',puntoPublico.X,',',puntoPublico.Y)
print('Punto privado: ',puntoPrivado.GetX(),',',puntoPrivado.GetY())
puntoPublico.X = 10
puntoPrivado.SetX(10)
print('Punto publico: ',puntoPublico.X,',',puntoPublico.Y)
print('Punto privado: ',puntoPrivado.GetX(),',',puntoPrivado.GetY())
