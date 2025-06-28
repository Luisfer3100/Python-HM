# Crear un diccionario llamado agenda y agragar al menos 3 contactos:
agenda = {'Luis':{'telefono':'6672919394', 'correo':'luisfernandoosal@gmail.com'}, 'Mara':{'telefono':'6674374508', 'correo':'maracard@icloud.com'}, 'Raul':{'telefono':'6672470706', 'correo':'raulocasio@gmail.com'}}

# Imprimir el numero de teléfono de un contacto especifico
print(agenda['Mara']['telefono'])

# Modificar el correo electronico de uno de los contactos
print(agenda['Luis']['correo'])

# Eliminar un contacto
del agenda['Raul']
print(agenda)

#Agregar un nuevo contacto desde el input del usuario
nombre = input('Cual es tu nombre? ')
telefono = input('¿Y tu numero de celular? ')
correo = input('Por ultimo tu correo por favor: ')

agenda[nombre] = {'telefono':telefono, 'correo':correo}
print(agenda)

# Usando get para buscar un contacto
print(agenda.get('Luis')) # Este es con uno que existe
print(agenda.get('Marco')) # Y este con uno que no

# Ahora usare el in para buscar el que no existe
if 'Marco' in agenda:
    print(agenda['Marco'])

# Mostrar todos los contactos con un for elegante
for nombre, datos in agenda.items():
    print(f'Contacto: {nombre}')
    print(f'  Teléfono: {datos["telefono"]}')
    print(f'  Correo: {datos["correo"]}\n')

# Recorre el siguiente diccionario e imprime algo como: "El producto Laptop cuesta 15000"
productos = {
    "Laptop": 15000,
    "Tablet": 8000,
    "Smartphone": 12000
}

for producto, precio in productos.items():
    print(f'El producto {producto} cuesta ${precio}')

# Crear un sistema simple de inventario para una tienda. Cada producto tendra: nombre del producto, precio y cantidad disponible.
inventario = {
    'iPhone':{'precio':12999, 'cantidad': 23},
    'macbook':{'precio':18899, 'cantidad':54},
    'homepod':{'precio':3499, 'cantidad': 12}
}

total_inventario = 0
for producto, precan in inventario.items():
    total_inventario+=precan['precio']*precan['cantidad']
    print(f'''
Producto: {producto}
    Precio: ${precan['precio']}
    Cantidad en stock: {precan['cantidad']}
''')

print(f'El total en pesos de tu inventario es de ${total_inventario}')
total = len(inventario)
print(f'El total de productos es: {total}')


