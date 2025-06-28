pedidos = [
    {"cliente": "Luis", "monto": 850.00},
    {"cliente": "Ana", "monto": 920.50},
    {"cliente": "Carlos", "monto": 300.00},
    {"cliente": "María", "monto": 850.00},
    {"cliente": "Jorge", "monto": 500.00}
]

def agregar_pedido(lista):
    lista = lista
    nombre = input('¿Cual es el nombre del cliente? ')
    monto = float(input('¿Cual es el monto del pedido? '))
    lista.append({'cliente':nombre, 'monto':monto})
    return lista

def calcular_media(lista):
    resultado = 0
    for n in lista:
        resultado += n['monto']
    resultado/=len(lista)
    return resultado

def calcular_mediana(lista):
    lista_montos = []
    for monto in lista:
        lista_montos.append(monto['monto'])

    lista_montos = sorted(lista_montos)
    largo = len(lista_montos)
    mitad = largo//2
    if largo%2==0:
        resultado = (lista_montos[mitad-1] + lista_montos[mitad])/2
    else:
        resultado = lista_montos[mitad]
    return resultado, lista_montos

def calcular_moda(lista):
    moda_lista = {}
    for n in lista:
        if n not in moda_lista:
            moda_lista[n] = 1
        else:
            moda_lista[n]+=1
    return max(moda_lista, key=moda_lista.get)

def clasificar_clientes(lista, media):
    clientes_vip = []
    clientes_normales = []
    for cliente in lista:
        if cliente['monto'] >= media:
            clientes_vip.append(cliente)
        else:
            clientes_normales.append(cliente)
    return clientes_vip, clientes_normales

mediana, lista = calcular_mediana(pedidos)
clientes_vip, clientes_normales = clasificar_clientes(pedidos,calcular_media(pedidos))


print('Estadisticas del pedido: ')
print(f'''
Media: ${calcular_media(pedidos):.2f}
Mediana: ${mediana:.2f}
Moda: ${calcular_moda(lista):.2f}''')

print(f'''
Clientes VIP: ''')
for cliente in clientes_vip:
    print(f"{cliente['cliente']} (${cliente['monto']})")

print(f'''
Clientes Normales: ''')
for cliente in clientes_normales:
    print(f"{cliente['cliente']} (${cliente['monto']})")

print(f'{len(pedidos)} pedidos')