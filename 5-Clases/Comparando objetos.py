# class Coordenadas:
#     def __init__(self, lat, lon):
#         self.lat = lat
#         self.lon = lon
#
# coord1 = Coordenadas(45, 80)
# coord2 = Coordenadas(45, 80)
# print(coord1, coord2)

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def __eq__(self, other):
        return (self.__nombre, self.edad) == (other.__nombre, other.edad)

p1 = Persona('Luis', 25)
p2 = Persona('Mara', 21)
print(p1 != p2)