import random
numero_veces = int(input('¿Cuantas veces lanzo el dado? '))
if numero_veces <=0:
    print('El numero de tiradas debe ser mayor a 0.')
else:

    def lanzar_dado(num_veces):
        tiradas = 0
        numeros_salidos = []

        while tiradas < num_veces:
            tiradas+=1
            numero = random.randint(1,6)
            numeros_salidos.append(numero)
            print(f'''
                Tirada #{tiradas}
                Cara del dado: {numero}''')

        numero_veces_count = [
            numeros_salidos.count(1),
            numeros_salidos.count(2),
            numeros_salidos.count(3),
            numeros_salidos.count(4),
            numeros_salidos.count(5),
            numeros_salidos.count(6)
        ]

        # Mostrar resultados
        for i, cantidad in enumerate(numero_veces_count):
            cara = i + 1
            porcentaje = (cantidad/numero_veces)*100
            print(f'El numero {cara} salio {cantidad} veces, lo que es un {porcentaje}%')


    lanzar_dado(numero_veces)