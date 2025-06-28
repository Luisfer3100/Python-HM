# Objetivo: Crear una clase Rectangulo que calcule el área automaticamente y valide los cambios en sus lados usando @property y @setter

class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def area(self):
        return self.__base*self.__altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, nueva_base):
        if nueva_base>0:
            self.__base = nueva_base
        else:
            print('La base debe ser mayor a 0.')

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, nueva_altura):
        if nueva_altura>0:
            self.__altura = nueva_altura
        else:
            print('La altura debe de ser mayor a 0.')

r = Rectangulo(4, 5)
print(r.area)     # 20

r.base = 10
r.altura = 2
print(r.area)     # 20

r.altura = -5     # ❌ Mensaje de error
print(r.area)     # 20 (no cambia)

