# crear un objeto o una instancia de la clase

class Punto:
    def __init__(self,x,y,):
        self.x = x
        self.y = y
    def MostrarPunto(self):
        print('El punto es (',self.x,',',self.y,')')

p1 = Punto(4,6)
p1.MostrarPunto()