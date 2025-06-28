productos = [
    {'codigo': 'A100', 'nombre': 'Laptop'},
    {'codigo': 'B200', 'nombre': 'Smartphone'},
    {'codigo': 'C300', 'nombre': 'Tablet'},
    {'codigo': 'D400', 'nombre': 'Monitor'},
    {'codigo': 'E500', 'nombre': 'Teclado'}
]

def buscar_producto_por_codigo(productos, codigo):
    for producto in productos:
        if producto['codigo'].lower() == codigo.lower():
            return producto
    return None

print(buscar_producto_por_codigo(productos, 'e500'))
