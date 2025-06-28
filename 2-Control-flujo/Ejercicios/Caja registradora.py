# Agregar una variable en la cual se ira agregando el coste total de la compra
total = 0

while True:
    costo_producto = input('¿Cual es el costo del producto? ')
    if costo_producto.lower()=='salir':
        break
    costo_producto = float(costo_producto)
    total+=costo_producto

print(f'El total de la compra es de ${total}')
