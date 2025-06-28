# 1. Eliminar los espacios en blanco un string y devolver una lista con los caracteres restantes.
string = 'Hola mundo'
# Eliminar espacios en blanco:
quitar_espacios = [n for n in string if n != ' ']

# 2. Contar en un diccionario cuanto se repiten los caracteres de un string.
contar_letras = {}
for n in quitar_espacios:
    valor=quitar_espacios.count(n)
    contar_letras[n] = valor

# 3. Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas.
dicc_tupla = []
for n in contar_letras.items():
    dicc_tupla.append(n)

# 4. De un listado de tuplas, devolver las tuplas que tengan el mayor valor.
tupla_mayor = []
max_valor = 0
for n in dicc_tupla:
    if n[1] > max_valor:
        tupla_mayor = [n]
        max_valor = n[1]
    elif n[1] == max_valor:
        tupla_mayor.append(n)

# 5. Crear un mensaje que diga: Los caracteres que mas se repiten con una cantidad de {cantidad} repeticiones son:
print(f'''
Los caracteres que mas se repiten con una cantidad de {tupla_mayor[0][1]} repeticiones son:''')
for n in tupla_mayor:
    print(f'- {n[0][0]}')

print(tupla_mayor)
print(contar_letras)
print(quitar_espacios)
print(dicc_tupla)
print('Ahora hazlo con funciones. Cambia cada uno de los pasos a funciones.')

