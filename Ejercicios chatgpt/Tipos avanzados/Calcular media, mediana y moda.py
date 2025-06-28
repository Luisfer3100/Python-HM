def media(datos):
    total = 0
    largo = len(datos)
    for n in datos:
        total+=n

    media = total/largo
    return (media)

def mediana(datos):
    lista_ordenada = sorted(datos)
    largo = len(lista_ordenada)
    mitad = largo//2
    if largo%2==0:
        return (lista_ordenada[mitad-1]+lista_ordenada[mitad])/2
    else:
        return lista_ordenada[mitad]

def moda(datos):
    modas = {}
    for n in datos:
        if n not in modas:
            modas[n] = 1
        else:
            modas[n] += 1
    return max(modas, key=modas.get)

calificaciones = [8.5, 9.0, 7.5, 10.0, 9.0, 8.5, 6.0]
print(f'''
La moda de las calificaciones del alumno Luis son: {moda(calificaciones)}
La media es de: {media(calificaciones)}
Y la mediana es de: {mediana(calificaciones)}''')