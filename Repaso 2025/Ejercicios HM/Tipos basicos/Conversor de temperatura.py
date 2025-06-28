# Pedir entrada de la temperatura
temp_c = int(input('Temperatura en °C: '))

# Conversion de temperaturas
temp_f = (temp_c*9/5) + 32
temp_k = temp_c + 273.15

# Dar salida a las temperaturas
print(f'''
Temperatura en °C: {temp_c}
Temperatura en °F: {temp_f}
Temperatura en °K: {temp_k}
''')
