lista_compras = [
    {'nombre':'tortillas de harina', 'precio':32},
    {'nombre':'queso chihuahua', 'precio':68},
    {'nombre':'jamon de pavo', 'precio':45},
    {'nombre':'manzana', 'precio':16},
    {'nombre':'pera','precio':12},
    {'nombre':'manzana','precio':16}
]

def ticket_compras(lista_compra):
    contador = {}
    for producto in lista_compra:
        nombre = producto['nombre']
        precio = producto['precio']
        if nombre in contador:
            contador[nombre]['cantidad']+=1
        else:
            contador[nombre] = {'precio':precio, 'cantidad':1}

    print(f'--------------------')
    print(f'| Ticket de compra |')
    print(f'--------------------')
    total=0
    for nombre, info in contador.items():
        precio = info['precio']
        cantidad = info['cantidad']
        subtotal = precio*cantidad
        total += subtotal
        print(f'{nombre} x{cantidad} - ${subtotal:.2f}')
    print(f'---------------------')
    print(f'|  Total: ${total:.2f}.  |')
    print(f'---------------------')

ticket_compras(lista_compras)