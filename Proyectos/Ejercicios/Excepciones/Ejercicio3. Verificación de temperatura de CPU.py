class OverheatingTemperature(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return self.mensaje

def check_cpu_temperature(temperatura):
    if temperatura >= 30 and temperatura <= 45:
        print(f'La temperatura de la CPU es de {temperatura}°C. Es normal en Reposo.')
    elif temperatura >= 50 and temperatura <= 70:
        print(f'La temperatura de la CPU es de {temperatura}°C. Es normal en uso moderado.')
    elif temperatura >= 70 and temperatura <= 85:
        raise OverheatingTemperature(f'La temperatura de la CPU es de {temperatura}°C, es alta.')
    elif temperatura>=90 and temperatura<=100:
        raise OverheatingTemperature(f'La temperatura es de {temperatura}, es muy alta.')
    elif temperatura>100:
        raise OverheatingTemperature('Temperatura arriba del limite seguro, apaga la computadora.')
    else:
        raise OverheatingTemperature('La temperatura es muy baja.')


try:
    temperatura_actual = 100 # Cambiar este valor para probar las diferentes excepciones.
    check_cpu_temperature(temperatura_actual)
except OverheatingTemperature as e:
    print(e)