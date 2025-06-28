class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def __del__(self):
        print( f'Adios perro 😞 {self.__nombre}')

    def __str__(self):
        return f'El perro se llama {self.__nombre} y tiene {self.edad} años.'


perro1 = Perro('Toby', 3)
print(perro1)
del perro1
# print(perro1)