class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    # def __str__(self):
    #     return f'el nombre de la persona es {self.__nombre} y tiene {self.edad} años.'

    def saludo(self):
        print(f'Hola {self.__nombre}.')


p1 = Persona('Luis', 25)
print(p1)  # El nombre de la persona es Luis y tiene 25 años.