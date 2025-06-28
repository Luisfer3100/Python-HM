class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'Producto: {self.nombre} - Precio: {self.precio}'


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)

p1 = Producto('iPhone', 23000)
p2 = Producto('PS5', 7500)
p3 = Producto('Lenovo YOGA', 23500)
p4 = Producto('Apple TV', 3499)

tecnologia = Categoria('Tecnologia', [p1,p2,p3])
tecnologia.agregar(p4)
tecnologia.imprimir()