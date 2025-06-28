cantidad = float(input('Dame la cantidad: '))
moneda = input('Ahora la moneda de origen: ')

if moneda.lower() == 'usd':
    print(f'{cantidad} {moneda} son: {cantidad*0.95} EUR y {cantidad*20.28} MXN')
elif moneda.lower() == 'eur':
    print(f'{cantidad} {moneda}: {cantidad*1.12} USD y {cantidad*21.36} MXN')
elif moneda.lower() == 'mxn':
    print(f'{cantidad} {moneda}: {cantidad*0.05} USD y {cantidad*0.05} EUR')
else:
    print('Divisa no válida. Porfavor, elige entre USD, EUR o MXN.')
