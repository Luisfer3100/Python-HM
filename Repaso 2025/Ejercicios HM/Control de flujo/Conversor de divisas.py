# Pedir al usuario la cantidad y nomeda
cantidad = float(input('Indicame la cantidad: '))
moneda = input('Indicame la moneda desde la cual convertiras: ').lower()

# Control de flujo
if cantidad > 0 and moneda == 'usd':
    print(f'{cantidad*0.95} EUR, {cantidad*20.28} MXN')
elif cantidad > 0 and moneda == 'eur':
    print(f'{cantidad * 1.12 } USD, {cantidad * 21.36} MXN')
elif cantidad > 0 and moneda == 'mxn':
    print(f'{cantidad * 0.05} USD, {cantidad * 0.05} EUR')
else:
    print('Divisa no valida. Porfavor, elige entre USD, EUR o MXN.')
