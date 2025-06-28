class CajaRegistradora:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({'nombre':nombre, 'precio':precio})

    def obtener_total(self):
        total = 0
        for producto in self.productos:
            total+=producto['precio']
        return total

    def dar_cambio(self, pago):
        if pago < self.obtener_total():
            return 'El pago es insuficiente.'
        else:
            cambio = pago-self.obtener_total()
            self.productos.clear()
            return cambio

    def listar_productos(self):
        lista = []
        for producto in self.productos:
            lista.append(producto['nombre'])

        return lista

class Cuentas:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, caja_registradora):
        lista_productos = caja_registradora.listar_productos()
        total = caja_registradora.obtener_total()
        self.cuentas.append({'productos':lista_productos, 'total':total})

    def obtener_total_cuentas(self):
        total = 0
        for cuenta in self.cuentas:
            total+= cuenta['total']
        return total

    def obtener_ticket_promedio(self):
        if not self.cuentas:
            return 0
        return self.obtener_total_cuentas() / len(self.cuentas)

    def listar_cuentas(self):
        return self.cuentas

caja = CajaRegistradora()
registro_cuentas = Cuentas()
caja.agregar_producto('Manzana', 0.5)
print("Total:", caja.obtener_total())
caja.agregar_producto('Pan', 1.0)
print(caja.listar_productos())

print("Total:", caja.obtener_total())
registro_cuentas.agregar_cuenta(caja)
print("Cambio:", caja.dar_cambio(2.0))
print(caja.listar_productos())

caja.agregar_producto('Leche', 1.5)
print("Total:", caja.obtener_total())
registro_cuentas.agregar_cuenta(caja)
print("Cambio:", caja.dar_cambio(3.0))
print(caja.listar_productos())

caja.agregar_producto('Huevos', 2.0)
caja.agregar_producto('Queso', 3.0)
caja.agregar_producto('Jamon', 4.0)
caja.agregar_producto('Pan', 1.0)
print("Total:", caja.obtener_total())
registro_cuentas.agregar_cuenta(caja)
print("Cambio:", caja.dar_cambio(10.0))

ticket_promedio_dia = registro_cuentas.obtener_ticket_promedio()
corte_dia = registro_cuentas.obtener_total_cuentas()
cuentas = registro_cuentas.listar_cuentas()
print("Cuentas del día:", cuentas)
print(f"El ticket promedio del día es de: {ticket_promedio_dia}")
print(f"El total de ventas del día es de: {corte_dia}")





