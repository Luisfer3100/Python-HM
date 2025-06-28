def es_palindromo(palabra):
    # Crear la funcion en el cual se eliminaran los espacios en blanco de la oracion
    palabra = palabra.lower()
    palabra = palabra.replace(' ', '')

    if palabra == palabra[::-1]:
        return True
    else:
        return False


print('Hola Mundo', es_palindromo('Hola mundo'))
print('Hola Mundo', es_palindromo('Anna'))
print('Hola Mundo', es_palindromo('oso'))