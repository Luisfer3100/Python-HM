# Preguntar cuanto es el total de la cuenta
total = input('¿Cuanto es el total a pagar? $').strip()
if total.lower()=='salir':
    exit()
total=float(total)

# Preguntar con cuanto pagara
pago = input('¿Con cuanto pagara el cliente? $').strip()
if pago.lower()=='salir':
    exit()
pago=float(pago)

if total == pago:
    print('El cliente ha pagado el monto exacto. No se requiere el cambio.')
elif pago > total:
    print(f'El cliente a pagado de mas, el cambio es de ${pago-total}')
elif pago < total:
    print(f'El cliente ha pagado menos, faltan ${total-pago}')
