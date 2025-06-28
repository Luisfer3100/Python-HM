# Objetivo: Crear una clase Fraccion que represente fracciones como 3/4, y puedeas:
# °Mostrarla como texto (__str__)
# °Sumar dos fracciones (__ad__)
# °Compararla si son iguales (__eq__)
# °Simplificar automaticamente si es posible
from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f'{self.numerador}/{self.denominador}'

    # def __add__(self, other):
    #     Fraccion(self.numerador + self.denominador)

    def __eq__(self, other):
        return self.numerador == self.denominador


