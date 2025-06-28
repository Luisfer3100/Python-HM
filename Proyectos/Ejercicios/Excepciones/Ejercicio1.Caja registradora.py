class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return self.mensaje

class CajaRegistradora:
    def __init__(self):
        self.lista = []

    def agregar_producto(self, nombre, precio):
        self.lista.append({'nombre':nombre, 'precio':precio})

    def calcular_total(self):
        total = 0
        for producto in self.lista:
            total+=producto['precio']

        return total

    def dar_cambio(self, pago):
        if pago < self.calcular_total():
            raise MiError('El pago es insuficiente.')
        return pago-self.calcular_total()

try:
    caja = CajaRegistradora()
    caja.agregar_producto('Manzana', 0.5)
    caja.agregar_producto('Pan', 1)
    print("Total:", caja.calcular_total())
    print("Cambio:", caja.dar_cambio(2))
    print("Cambio:", caja.dar_cambio(1))
except MiError as e:
    print(e)
finally:
    print('Acabo el programa.')