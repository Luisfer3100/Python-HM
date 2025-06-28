lista_compras = [
    {'nombre': 'pepino', 'precio': 10.00},
    {'nombre': 'pepino', 'precio': 10.00},
    {'nombre': 'manzana', 'precio': 12.50}
]

def ticket(productos):
    contador_productos = {} # Variable de tipo dicc, para aqui crear un diccionario que contenga el nombre del producto, precio y cuantas veces esta en la lista
    for producto in productos:
        nombre = producto['nombre']
        precio = producto['precio']
        if nombre in contador_productos: # Aqui condicionaremos si el elemento con dicho nombre ya esta dentro de la variable dicc, solo sume a la key de 'cantidad'
            # una sola unidad
            contador_productos[nombre]['cantidad'] += 1
        else:
            contador_productos[nombre] = {'precio':precio, 'cantidad':1} # Y aqui si no se encuentra aun en la variable de dicc, cree un nuevo dicc con el nombre
            # de la key y de valor tendra un diccionario con keys de precio y cantidad y sus id respectivos.

    print(f'''
    ----------------------
       Ticket de compra
    ----------------------''')
    total = 0 # Esta sera la variable para el total de la compra
    for n, i in contador_productos.items(): # En este for desempaquetamos con dos variables (n, i), y usamos .items para volver tuplas el dicc.
        precio = i['precio'] # Precio sera igual a i(la cual accede a el id, en el que viene precio y cantidad) y le daremos de valor el id de precio
        cantidad = i['cantidad'] # Seria el mismo caso que el de precio pero con el valor de cantidad
        subtotal = precio*cantidad # EL subtotal es el total por articulo, por lo cual se multiplica el precio de un producto por las veces que se comprara
        total += subtotal # el total sera la suma de todos los subtotales de los productos
        print(f'{n} x{cantidad} -${subtotal:.2f}')
    print(f'''
    ----------------------
      Total: {total:.2f}''')

ticket(lista_compras)