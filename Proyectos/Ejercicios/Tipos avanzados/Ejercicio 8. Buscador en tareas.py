tareas = [
    {'id':1, 'descripcion':'Lavar los platos'},
    {'id':2, 'descripcion':'Lavar los platos'},
    {'id':3, 'descripcion':'Lavar los platos'},
    {'id':4, 'descripcion':'Lavar los platos'},
    {'id':5, 'descripcion':'Lavar los platos'},
    {'id':6, 'descripcion':'Lavar los platos'},
    {'id':7, 'descripcion':'Lavar los platos'},
    {'id':8, 'descripcion':'Lavar los platos'},
    {'id':9, 'descripcion':'Lavar los platos'},
    {'id':10, 'descripcion':'Lavar los platos'}
]

def buscar_tarea_por_id(tareas, id):
    for tarea in tareas:
        if tarea['id'] == id:
            return tarea
    return None

def buscar_tarea_por_texto(tareas, texto):
    tareas_encontradas = []
    for tarea in tareas:
        if texto.lower() in tarea['descripcion'].lower():
            tareas_encontradas.append(tarea)
    return tareas_encontradas

print(buscar_tarea_por_id(tareas, 7))
