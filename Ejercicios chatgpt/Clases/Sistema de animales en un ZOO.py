from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def emitir_sonido(self):
        pass

    @abstractmethod
    def tipo(self):
        pass

class Perro(Animal):

    def emitir_sonido(self):
        return 'Guau!'

    def tipo(self):
        return 'Mamifero'

class Mono(Animal):
    def emitir_sonido(self):
        return 'Uhh uhh ahh ahh'

    def tipo(self):
        return 'Mamifero'

class Loro(Animal):
    def emitir_sonido(self):
        return 'Hola, soy un Loro'

    def tipo(self):
        return 'Ave'

animales = [
    Perro("Max", 5),
    Loro("Paco", 2),
    Mono("George", 3)
]
for animal in animales:
    print(f"{animal.nombre}, {animal.tipo()}, dice: {animal.emitir_sonido()}")
