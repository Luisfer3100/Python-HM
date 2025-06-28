empleados = [
    {'nombre': 'Ana', 'departamento': 'ventas', 'antiguedad': 5},
    {'nombre': 'Luis', 'departamento': 'marketing', 'antiguedad': 2},
    {'nombre': 'Carlos', 'departamento': 'ventas', 'antiguedad': 7},
    {'nombre': 'Sofía', 'departamento': 'recursos humanos', 'antiguedad': 3},
    {'nombre': 'Diego', 'departamento': 'ventas', 'antiguedad': 1}
]

def filtrar_empleados(empleados, departamento, antiguedad):
    empleados_aplicados = []
    for empleado in empleados:
        if empleado['departamento'].lower() == departamento.lower() and empleado['antiguedad'] >= antiguedad:
            empleados_aplicados.append(empleado)
    return empleados_aplicados

print(filtrar_empleados(empleados,'ventas', 3))
