class Hotel:
    def __init__(self):
        self.__NumeroHabitaciones = 0
        self.__Estrellas = 0
    def SetNumeroHabitaciones(self,habitaciones):
        self.__NumeroHabitaciones = habitaciones
    def SetEstrellas(self,estrellas):
        self.__Estrellas = estrellas
    def MostrarHotel(self):
        print('*** HOTEL ***')
        print('\tEstrellas: ',self.__Estrellas)
        print('\tHabitaciones: ',self.__NumeroHabitaciones)

class Restaurante:
    def __init__(self):
        self.__Tenedores = 0
        self.__HoraApertura = 0
    def SetTenedores(self,tenedores):
        self.__Tenedores = tenedores
    def SetHoraApertura(self,horaApertura):
        self.__HoraApertura = horaApertura
    def MostrarRestaurante(self):
        print('*** RESTAURANTE ***')
        print('\tHora apertura: ',self.__HoraApertura)
        print('\tTenedores: ',self.__Tenedores)

class Negocio(Hotel,Restaurante):
    def __init__(self):
        self.__Nombre = 0
        self.__Direccion = 0
        self.__Telefono = 0
    def SetNombre(self,nombre):
        self.__Nombre = nombre
    def SetDireccion(self,direccion):
        self.__Direccion = direccion
    def SetTelefono(self,telefono):
        self.__Telefono = telefono
    def MostrarNegocio(self):
        print('*** NEGOCIO ***')
        print('\tNombre: ',self.__Nombre)
        print('\tDireccion: ',self.__Direccion)
        print('\tTelefono: ',self.__Telefono)
        self.MostrarHotel()
        self.MostrarRestaurante()

negocio1 = Negocio()
negocio1.SetNombre('Ibis')
negocio1.SetDireccion('Blvd. Rosales')
negocio1.SetTelefono('6688784596')
negocio1.SetNumeroHabitaciones('80')
negocio1.SetEstrellas('5')
negocio1.SetTenedores('3')
negocio1.SetHoraApertura('8:00 am')
negocio2 = Negocio()
negocio2.SetNombre('El Dorado')
negocio2.SetDireccion('Calle Gabriel Leyva')
negocio2.SetTelefono('6681129685')
negocio2.SetNumeroHabitaciones('60')
negocio2.SetEstrellas('3')
negocio2.SetTenedores('2')
negocio2.SetHoraApertura('5:00 am')
negocio1.MostrarNegocio()
negocio2.MostrarNegocio()