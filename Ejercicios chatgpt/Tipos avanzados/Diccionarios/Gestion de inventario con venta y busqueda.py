inventario = {
    'iPhone': {'precio': 12999, 'cantidad': 23},
    'macbook': {'precio': 18899, 'cantidad': 54},
    'homepod': {'precio': 3499, 'cantidad': 12}
}

# Pedir al usuario un nombre de producto, si existe, mustra el precio y cantidad. Si no existe, muestra un mensaje como: "Ese producto no esta en el inventario."
producto_a_buscar = input('¿Que producto quieres buscar? ')

if producto_a_buscar in inventario:
    datos = inventario[producto_a_buscar]
    print(f'''
El precio del producto es de ${datos['precio']}
Y la cantidad en stock es de {datos['cantidad']}
''')
else:
    print('Este producto no esta en el inventario.')

# Registrar una venta
producto_a_vender = input('¿Que producto venderas? ')
cantidad_a_vender = int(input('¿Cuantas piezas venderas? '))

if producto_a_vender in inventario:
    datos = inventario[producto_a_vender]
    cantidad_exis = datos['cantidad']

    if cantidad_a_vender <= cantidad_exis and cantidad_a_vender>0:
        datos['cantidad']-=cantidad_a_vender
    else:
        print('No hay suficientes unidades disponibles.')
else:
    print('Este producto no esta en el inventario.')

# Mostrar el inventario actualizado despues de la compra
print('El inventario se actualizo:')
for n,i in inventario.items():
    print(f"Hay {i['cantidad']} {n}")