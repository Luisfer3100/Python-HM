compras = {
    'Cliente1': 200,
    'Cliente2': 100,
    'Cliente3': 180
}
def aplicar_promocion(compra):
    clientes_con_promocion = []
    descuento_aplicado = {}
    for cliente, total in compra.items():
        cliente_id = cliente
        total = total
        if total >= 180:
            clientes_con_promocion.append(cliente_id)
            total_desc = (total*10)/100
            descuento_aplicado[cliente_id] = total-total_desc
    return clientes_con_promocion, descuento_aplicado



print(aplicar_promocion(compras))