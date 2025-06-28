class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def presentar_perro(self):
        print(f'Este es mi perro. Tiene {self.edad} año(s), su nombre es {self.nombre} y es de la raza {self.raza}')

mi_perro = Perro('Toby', 'Fernch', 1)
mi_perro.presentar_perro()
