# Solicitar cantidad de moneda local (MXN)
moneda_mxn = int(input('Dame la cantidad a convertir: '))

# Hacer la conversion a las monedas
USD = moneda_mxn/19.37
EUR = moneda_mxn/21.67
GBP = moneda_mxn/25.70
JPY = moneda_mxn/0.13

# Mostrar los resultados de lsa conversiones
print(f'''
Los ${moneda_mxn} en MXN serian:
{USD} USD
{EUR} EUR
{GBP} GBP
{JPY} JPY
''')
