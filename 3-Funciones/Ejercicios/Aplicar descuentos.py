# definir la funcion para el descuento
def descuento(total, porcentaje):
    if total <= 0:
        return 'El precio original debe ser mayor a 0.'

    if porcentaje <= 0 or porcentaje >= 100:
        return 'Este porcentaje de descuento no es valido.'
    else:
        precio_final = total - (total * porcentaje / 100)
        return f'El precio inicial era de ${total}, el porcentaje de descuento que se aplico fue de {porcentaje}%. El precio final es de ${precio_final}.'

total = float(input('¿Cual es el precio original a pagar? '))
porcentaje = float(input('¿Cuanto porcentaje se le aplicara? '))

print(descuento(total, porcentaje))

