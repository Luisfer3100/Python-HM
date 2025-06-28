# Crear un diccionario llamado libros que tenga: 3 libros como clave y cada libro tener un diccionario con autor y año.
libros = {
    'La teoria del todo':{'autor': 'S. Hawking', 'año': 2002},
    'Diario de Greg: Dia de perros':{'autor':'Jeff Kinney', 'año': 2009},
    'Habitos atomicos':{'autor':'James Clear', 'año':2018}
}

# Recorrerlo con un for y mostrar de forma elegante esos datos.
for nombre, datos in libros.items():
    print(f'''
Libro: {nombre}
    Autor: {datos['autor']}
    Año: {datos['año']}
''')

# Agregar un nuevo libro con input
nuevo_libro = input('Ingresa un nuevo libro: ')
autor = input('¿De que autor es? ')
año = int(input('¿En que año se publico? '))
libros[nuevo_libro] = {'autor':autor, 'año':año}
print(libros)

# Eliminar un libro del diccionario
libro_del = input('¿Qué libro quieres eliminar? ').lower()
if libro_del not in libros:
    print('No existe dicho libro.')
else:
    del libros[libro_del]
    print(libros)
