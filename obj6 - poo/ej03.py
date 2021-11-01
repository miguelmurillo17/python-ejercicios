# asignar un objeto a otro objeto

class Punto:
    def __init__(self,x,y,):
        self.X = x
        self.Y = y

    def MostrarPunto(self):
        print('El punto es (',self.X,',',self.Y,')')
        
    def __str__(self):
        cadena = '[' + str(self.X) + ',' + str(self.Y) + ']'
        return(cadena)

p1 = Punto(4,5)
p1.MostrarPunto()
p2 = Punto(6,7)
p2.MostrarPunto()
p1 = p2
p1.MostrarPunto()
print(p1)