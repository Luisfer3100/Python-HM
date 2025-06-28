estudiantes = [
    {'matricula': 101, 'nombre': 'Ana'},
    {'matricula': 102, 'nombre': 'Luis'},
    {'matricula': 103, 'nombre': 'Carlos'},
    {'matricula': 104, 'nombre': 'Sofía'},
    {'matricula': 105, 'nombre': 'Diego'}
]

def buscar_estudiante_por_matricula(estudiantes, matricula):
    for n in estudiantes:
        if n['matricula'] == matricula:
            return n
    return None

print(buscar_estudiante_por_matricula(estudiantes, 102))
