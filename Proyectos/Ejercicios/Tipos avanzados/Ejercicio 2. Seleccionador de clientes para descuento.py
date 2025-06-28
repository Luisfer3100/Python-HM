compras =[
    {'cliente':'cliente1', 'total': 150},
    {'cliente':'cliente2', 'total': 110},
    {'cliente':'cliente3', 'total': 180},
    {'cliente':'cliente4', 'total': 200},
    {'cliente':'cliente5', 'total': 80}
]
def descuento(compras):
    clientes_si = {}
    for n in compras:
        cliente = n['cliente']
        precio = n['total']
        if precio >= 180:
            clientes_si[cliente] = precio
    return clientes_si


clientes_promocion = descuento(compras)
print(f'Los clientes que si entran en promoción son: {clientes_promocion}')
