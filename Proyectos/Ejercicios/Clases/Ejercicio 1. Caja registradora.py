from distutils.command.clean import clean
from os import remove


class CajaRegistradora:
    cambio = 0
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({'nombre':nombre, 'precio':precio})

    def obtener_total(self):
        total = 0
        for producto in self.productos:
            total+= producto['precio']
        return total

    def dar_cambio(self, pago):
        cambio = 0
        if pago < self.obtener_total():
            return 'Pago insuficiente.'
        else:
            cambio = pago - self.obtener_total()
            self.productos.clear()
            return cambio


    def listar_productos(self):
        lista = []
        for producto in self.productos:
            lista.append(producto['nombre'])
        return lista

productos = CajaRegistradora()
productos.agregar_producto('Manzana', 0.5)
productos.agregar_producto('Pan', 1.0)
print(productos.obtener_total())

print(productos.dar_cambio(2.0))

print(productos.listar_productos())