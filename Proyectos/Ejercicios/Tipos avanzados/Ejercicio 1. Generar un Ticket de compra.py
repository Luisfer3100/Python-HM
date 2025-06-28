# Crearemos una función en la cual, generaremos un ticket de compra.
lista_compras =[
    {'nombre':'pepino', 'precio': 10.00},
    {'nombre':'pepino', 'precio': 10.00},
    {'nombre':'manzana', 'precio': 12.50},
    {'nombre':'mango', 'precio': 32.50},
]
def generar_ticket(lista_compras):
    contador_productos = {}
    total = 0
    for n in lista_compras:
        nombre = n['nombre']
        if nombre in contador_productos:
            contador_productos[nombre]['cantidad'] += 1
        else:
            contador_productos[nombre] = {'precio': n['precio'], 'cantidad':1}

    print(f'''
    ----------------
    Ticket de compra
    ----------------''')
    for n, i in contador_productos.items():
        precio = i['precio']
        cantidad = i['cantidad']
        subtotal = precio*cantidad
        total += subtotal
        print(f'{n} x{cantidad} - ${subtotal:.2f}')
    print(f'''
    ----------------
    Total: ${total:.2f}
    ----------------
    ''')

generar_ticket(lista_compras)
