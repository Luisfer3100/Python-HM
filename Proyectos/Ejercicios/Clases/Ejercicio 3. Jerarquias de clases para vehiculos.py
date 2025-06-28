from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def descripcion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}."

class Coche(Vehiculo):
    def descripcion(self):
        return f"Coche - {super().descripcion()}"

class Moto(Vehiculo):
    def descripcion(self):
        return f"Moto - {super().descripcion()}"

class Bicicleta(Vehiculo):
    def descripcion(self):
        return f"Bicicleta - {super().descripcion()}"

coche = Coche('Nissan', 'Versa')
moto = Moto('Yamaha', 'MT-07')
bici = Bicicleta('Giant', 'Escape 3')

print(coche.descripcion())
print(moto.descripcion())
print(bici.descripcion())
