import random
def tirar_dados(veces):
    contador = veces
    caras_salidas = []
    while contador>0:
        contador-=1
        dado = random.randint(1,6)
        caras_salidas.append(dado)
    print(caras_salidas)

    veces_salidas = {}
    for n in caras_salidas:
        i = caras_salidas.count(n)
        if n not in veces_salidas:
            veces_salidas[n] = i

    for n, i in veces_salidas.items():
        print(f'Cara {n} salio {i} veces: {(i/veces)*100:.2f}%')



tirar_dados(6)
