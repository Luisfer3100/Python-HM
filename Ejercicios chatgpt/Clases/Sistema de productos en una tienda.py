# Objetivo: Crear una clase Producto que representa un artículo en venta.
class Producto:
    impuesto = 0.16
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    def precio_total(self):
        total = (self.precio_base * self.impuesto) + self.precio_base
        return total

    @classmethod
    def cambiar_impuesto(cls, nueva_tasa):
        cls.impuesto = nueva_tasa

p1 = Producto('Zapatos', 1000)
p2 = Producto('Camisa', 500)

print(p1.precio_total())
print(p2.precio_total())

Producto.cambiar_impuesto(0.12)
p3 = Producto('Zapatos', 1000)
p4 = Producto('Camisa', 500)

print(p3.precio_total())
print(p4.precio_total())

