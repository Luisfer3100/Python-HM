from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(cls):
        pass

class Perico(Animal):
    def sonido(cls):
        print('Hola, soy un perico.')

class Perro(Animal):
    def sonido(cls):
        print('Guau!')

perro = Perro()
perro.sonido()

perico = Perico()
perico.sonido()
