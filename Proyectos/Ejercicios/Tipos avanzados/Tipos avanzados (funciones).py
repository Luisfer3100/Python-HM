# Eliminar los espacios en blanco un string y devolver una lista con los caracteres restantes.
def eliminar_espacios(string):
    quitar_estapcios = [n for n in string if n != ' ']
    return quitar_estapcios

# Contar en un diccionario cuanto se repiten los caracteres de un string
def contar_letras(funcion):
    contar_letra = {}
    for n in funcion:
        valor=funcion.count(n)
        contar_letra[n]=valor
    return contar_letra

# Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas.
def ordenar(contar_letras):
    dicc_tupla = []
    for n in contar_letras.items():
        dicc_tupla.append(n)
    return dicc_tupla

# De un listado de tuplas, devolver las tuplas que tengan el mayor valor
def mayor_valor(ordenar):
    tupla_mayor = []
    max_valor = 0
    for n in ordenar:
        if n[1] > max_valor:
            tupla_mayor = [n]
            max_valor = n[1]
        elif n[1] == max_valor:
            tupla_mayor.append(n)
    return tupla_mayor

eliminar = eliminar_espacios('Hola mundo ')
contar = contar_letras(eliminar)
ordenar = ordenar(contar)
mayor = mayor_valor(ordenar)

# Crear un mensaje que diga: Los caracteres que mas se repiten con una cantidad de {cantidad} repeticiones son:
print(f'''
Los caracteres que mas se repiten con una cantidad de {mayor[0][1]} repeticiones son:''')
for n in mayor:
    print(f'- {n[0][0]}')