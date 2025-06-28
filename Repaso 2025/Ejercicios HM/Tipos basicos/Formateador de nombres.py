# Entrada de los nombres y apellidos. Tambien en este script se usara metodos para modificar espacios en blanco y la mayuscula en cada palabra.
nombre1 = str(input('Primer nombre: ')).strip().capitalize()
nombre2 = str(input('Segundo nombre: ')).strip().capitalize()
apellido1 = str(input('Primer apellido: ')).strip().capitalize()
apellido2 = str(input('Segundo apellido: ')).strip().capitalize()

# Definir y dar valor a variable con el nombre completo
nombre_completo = f'{nombre1} {nombre2} {apellido1} {apellido2}'.replace('  ', '')

# Imprimir el nombre completo ya formateado
print(nombre_completo)
