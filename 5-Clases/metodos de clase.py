class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar_perro(self):
        print(f'Este es mi perro {self.nombre} y tiene {self.edad} año(s).')

    @classmethod
    def factory(cls):
        return cls('Toby', 3)

mi_perro = Perro.factory()
print(mi_perro.edad, mi_perro.nombre)