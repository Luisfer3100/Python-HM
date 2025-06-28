tareas = [
    {'id':1, 'descripcion':'Lavar los platos'},
    {'id':2, 'descripcion':'Lavar la ropa'},
    {'id':3, 'descripcion':'Lavar el baño'},
    {'id':4, 'descripcion':'Barrer la casa'},
    {'id':5, 'descripcion':'Trapear la casa'},
    {'id':6, 'descripcion':'Sacudir los muebles'},
    {'id':7, 'descripcion':'Limpiar los cristales'},
    {'id':8, 'descripcion':'Sacar la basura'},
    {'id':9, 'descripcion':'Regar las plantas'},
    {'id':10, 'descripcion':'Lavar el carro'}
]

def buscar_por_id(tareas, id):
    for tarea in tareas:
        if tarea['id'] == id:
            return tarea
    return None

def buscar_por_texto(tareas, texto):
    tarea_text = []
    for tarea in tareas:
        if texto.lower() in tarea['descripcion'].lower():
            tarea_text.append(tarea)
    return tarea_text

print(buscar_por_id(tareas, 5))
print(buscar_por_texto(tareas, 're'))
