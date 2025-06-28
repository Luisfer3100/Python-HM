estudiantes = [
    {"nombre": "Luis", "calificacion": 8.5},
    {"nombre": "Ana", "calificacion": 9.0},
    {"nombre": "Carlos", "calificacion": 5.5},
    {"nombre": "María", "calificacion": 8.5},
    {"nombre": "Jorge", "calificacion": 6.0}
]

def agregar_estudiante(lista):
    lista = lista
    estudiante = input('Dame el nombre: ').capitalize()
    califi = float(input('Ahora su calificación: '))
    lista.append({'nombre':estudiante, 'calificacion':califi})
    print(lista)

def calcular_media(lista):
    calificaciones = []
    for alumno in lista:
        calificaciones.append(alumno.get('calificacion'))
    resultado= 0
    for calificacion in calificaciones:
        resultado+=calificacion
    return resultado/len(calificaciones), calificaciones

def calcular_mediana(lista):
    resultado = 0
    lista = sorted(lista)
    largo = len(lista)
    mitad = largo//2
    if largo%2==0:
        resultado = (lista[mitad-1] + lista[mitad])/2
    else:
        resultado = lista[mitad]
    return resultado

def calcular_moda(lista):
    modas = {}
    for calificacion in lista_calificaciones:
        if calificacion not in modas:
            modas[calificacion] = 1
        else:
            modas[calificacion]+=1
    return max(modas, key=modas.get)

def aprobados_reprobados(lista):
    aprobados = []
    reprobados = []
    for n in lista:
        if n.get('calificacion') >= 6.0:
            aprobados.append(n.get('nombre'))
        else:
            reprobados.append(n.get('nombre'))
    return aprobados, reprobados

media, lista_calificaciones = calcular_media(estudiantes)
mediana = calcular_mediana(lista_calificaciones)
moda = calcular_moda(lista_calificaciones)
aprobados, reprobados = aprobados_reprobados(estudiantes)
print(f'La media de las calificaciones son: {media}')
print(f'La mediana es: {mediana}')
print(f'La moda es: {moda}')
print('Aprobados: ')
for n in aprobados:
    if n == aprobados[-1]:
        print(f'''-{n}
''')
    else:
        print(f'-{n}')
print('Reprobados: ')
for n in reprobados:
    if n == reprobados[-1]:
        print(f'''-{n}
''')
    else:
        print(f'-{n}')

agregar_estudiante(estudiantes)