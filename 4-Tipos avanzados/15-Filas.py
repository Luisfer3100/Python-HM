from collections import deque
lista = [1,2,3]
fila = deque(lista)

# Agregar elemento
fila.append(4)
fila.append(5)
fila.append(6)
print(lista)

# Eliminar elemento, respetando los FIFO
fila.popleft()
print(fila)

fila.popleft()
print(fila)
fila.popleft()
print(fila)
fila.popleft()
print(fila)
fila.popleft()
print(fila)
fila.popleft()
print(fila)
# Condicionaremos a que si la fila esta vacia, nos imprima un mensaje
if not fila:
    print('La fila esta vacia.')
