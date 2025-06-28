compras = {
    'Cliente1': 200,
    'Cliente2': 100,
    'Cliente3': 180
}

def calcular_costo_promocion(compras):
    clientes_aprobados = []
    descuento_total = 0
    for cliente, total in compras.items():
        if total >= 180:
            clientes_aprobados.append(cliente)
            descuento_total += (total*10)/100
    return  descuento_total


print(f'El descuento total es de: ${calcular_costo_promocion(compras)}')