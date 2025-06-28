class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona1 = Persona('Luis', 25)
print(persona1.nombre)


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad


persona1 = Persona('Luis', 25)
#print(persona1.__nombre)
print(persona1._Persona__nombre)


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre


persona1 = Persona('Luis', 25)
print(persona1.get_nombre())


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre


persona1 = Persona('Luis', 25)
print(persona1.get_nombre())  # Luis
persona1.set_nombre('Fernando')
print(persona1.get_nombre())  # Fernando
