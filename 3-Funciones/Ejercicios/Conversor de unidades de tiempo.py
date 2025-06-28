# Definir las 3 funciones
# funcion que convierte una cantidad y unidad dada a segundos
def a_segundos(cantidad, unidad):
    if unidad.lower() == 'segundo':
        return 'La unidad que quieres convertir a segundos ya son segundos.'
    elif unidad.lower() == 'minuto':
        cantidad = cantidad*60
    elif unidad.lower() == 'hora':
        cantidad = cantidad*3600
    elif unidad.lower() == 'dia':
        cantidad *= 86400
    elif unidad.lower() == 'mes':
        cantidad *= 2592000
    elif unidad.lower() == 'año':
        cantidad *= 31536000
    else:
        return 'Error'

    return cantidad

def de_segundos(cantidad, unidad):
    if unidad.lower() == 'segundo':
        return cantidad
    elif unidad.lower() == 'minuto':
        cantidad/=60
    elif unidad.lower() == 'hora':
        cantidad/=3600
    elif unidad.lower() == 'dia':
        cantidad /= 86400
    elif unidad.lower() == 'mes':
        cantidad /= 2592000
    elif unidad.lower() == 'año':
        cantidad /= 31536000
    else:
        return 'Error'

    return cantidad

def convertir_tiempo(cantidad, unidad_origen, unidad_destino):
    cantidad_en_segundos = a_segundos(cantidad, unidad_origen)
    if cantidad_en_segundos == 'Error':
        return'Unidad de tiempo no valida.'
    cantidad_convertida = de_segundos(cantidad_en_segundos, unidad_destino)
    return f'{cantidad} {unidad_origen}(s) son {cantidad_convertida} {unidad_destino}(s).'




print(convertir_tiempo(100, 'hora', 'dia'))