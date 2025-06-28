cursos = [
{'nombre': 'HTML: Sin Fronteras', 'estado': 'en progreso'},
{'nombre': 'CSS3: Sin Fronteras', 'estado': 'completado'},
{'nombre': 'SQL: Sin fronteras', 'estado': 'no iniciado'},
{'nombre': 'Python: HTML, CSS, Flask, MySQL', 'estado': 'en progreso'},
{"nombre": "Aprende Javascript, HTML5, CSS3 y NodeJS desde cero", "estado": "completado"},
{"nombre": "React - Guía definitiva: hooks, router, redux, next + Proyectos", "estado": "no iniciado"},
{"nombre": "TypeScript: sin fronteras", "estado": "completado"},
{"nombre": "Ultimate Python", "estado": "en progreso"},
{"nombre": "Ultimate Linux", "estado": "completado"},
{"nombre": "Ultimate Docker", "estado": "no iniciado"},
{"nombre": "Ultimate GIT + GITHUB", "estado": "en progreso"},
{"nombre": "Ultimate JavaScript", "estado": "completado"},
{"nombre": "Ultimate React", "estado": "no iniciado"},
{"nombre": "Ultimate Java", "estado": "en progreso"}
]

def filtrar_cursos(cursos):
    lista_progreso = []
    lista_completado = []
    lista_no_iniciado = []
    for n in cursos:
        if n['estado'] == 'en progreso':
            lista_progreso.append(n['nombre'])
        elif n['estado'] == 'completado':
            lista_completado.append(n['nombre'])
        elif n['estado'] == 'no iniciado':
            lista_no_iniciado.append(n['nombre'])
    print(f'''
Cursos en progreso:''')
    for n in lista_progreso:
        print(f'{n}')
    print('\nCursos completados: ')
    for n in lista_completado:
        print(f'{n}')
    print('\nCursos no iniciados:')
    for n in lista_no_iniciado:
        print(f'{n}')

filtrar_cursos(cursos)