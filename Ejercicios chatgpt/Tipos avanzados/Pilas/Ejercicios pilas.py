# Simular una pila de platos
platos = [1,2,3,4,5]

# Agregar platos
platos.append(6)
platos.append(7)
platos.append(8)

# Quitar platos hasta llegar al indicado
platos_levantados = []
plato_esperado = []
for n in platos[::-1]:
    if n != 3:
        platos_levantados = platos.pop()
    else:
        plato_esperado.append(n)
        break

# Regresar los platos levantados
for n in platos_levantados:
    platos.append(n)

print(platos)
