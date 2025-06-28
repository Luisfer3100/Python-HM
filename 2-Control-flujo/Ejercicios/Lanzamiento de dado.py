# Importar libreria random
import random

# Pedir al usuario el numero de veces que se tirara el dado
veces_tirar_dado = int(input('¿Cuantas veces quieres tirar el dado? '))
if veces_tirar_dado <= 0:
    print('El numero de lanzamientos debe ser mayor a 0')
    exit()
tirada = 0
numeros_salidos = []

while tirada < veces_tirar_dado:
    tirada += 1
    # Numero aleatorio del 1 al 6
    numero = random.randint(1, 6)
    print(f'''
    Tirada #{tirada}
    Cara del dado: {numero}''')
    numeros_salidos.append(numero)

numero_veces = [
    numeros_salidos.count(1),
    numeros_salidos.count(2),
    numeros_salidos.count(3),
    numeros_salidos.count(4),
    numeros_salidos.count(5),
    numeros_salidos.count(6)
]

# Mostrar resultados
for i, cantidad in enumerate(numero_veces):
    cara = i+1
    porcentaje = (cantidad/veces_tirar_dado)*100
    print(f'El numero {cara} salio {cantidad} veces, lo que es un {porcentaje}%')
