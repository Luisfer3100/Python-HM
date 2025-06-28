# Objetivo: Crear una clase SalaCine que permita registrar películas, asientos disponibles y realizar reservas de personas.

class SalaCine:
    total_salas = 0

    def __init__(self, pelicula, asientos):
        self.pelicula = pelicula
        self.asientos = asientos
        self.reservaciones = []
        SalaCine.total_salas = self.total_salas+1

    def reservar(self,nombre_cliente):
        if self.asientos > 0:
            self.reservaciones.append(nombre_cliente)
            self.asientos-=1
        else:
            return 'No hay asientos disponibles.'

    def asientos_disponibles(self):
        print( self.asientos)

    def mostrar_reservaciones(self):
        print('Clientes que han reservado: ')
        for nombre in self.reservaciones:
            print(nombre)

    @classmethod
    def total_salas_registradas(cls):
        return f'El total de salas son: {cls.total_salas}'

lista_clientes = ['Luis', 'Mara']
sala1 = SalaCine('Spider-man', 3)
sala1.reservar('Itzel')
sala1.reservar('Pau')
sala1.reservar('Jesus')
sala1.reservar('Patsy')
sala1.mostrar_reservaciones()

sala2 = SalaCine('El conjuro', 2)
sala2.reservar('Luis')
sala2.reservar('Carlos')
sala2.asientos_disponibles()
print(SalaCine.total_salas_registradas())