from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def moverse(self):
        pass

class Auto(Transporte):
    def moverse(self):
        return 'El auto se esta moviendo.'

class Tren(Transporte):
    def moverse(self):
        return  'El tren de esta moviendo.'

class Avion(Transporte):
    def moverse(self):
        return 'El avion se esta moviendo.'

class Persona(Transporte):
    def moverse(self):
        return 'La persona se esta moviendo.'

def simular_movimiento(objeto):
    return objeto.moverse()

auto = Auto()
tren = Tren()
avion = Avion()
persona = Persona()

print(simular_movimiento(auto))
print(simular_movimiento(tren))
print(simular_movimiento(avion))
print(simular_movimiento(persona))
