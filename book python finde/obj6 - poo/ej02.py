# crear varios objetos o instancias de una clase

class Punto:
    def __init__(self,x,y,):
        self.X = x
        self.Y = y
    def MostrarPunto(self):
        print('El punto es (',self.X,',',self.Y,')')

p1 = Punto(4,61)
p2 = Punto(5,4)
p3 = Punto(42,8)
p4 = Punto(-4,-2)

p1.MostrarPunto()
p2.MostrarPunto()
p3.MostrarPunto()
p4.MostrarPunto()
