# Los operadores lógicos nos sirven para hacer de nuestras estructuras mas estrictas.

# and, esta ejecutara la condicion solo si ambas son True
edad = 24
carro = True

if edad > 17 and carro:
    print('Puedes manejar')

# or, se ejecutara la condicion si al menos una de las 2 es True:
edad = 24
carro = False

if edad > 17 or carro:
    print('Puedes manejar')

# not
edad = 15
carro = False

if not carro and not edad>17:
    print('No Puedes manejar')

# Condiciones dentro de parentesis
edad = 22
carro = True
gasolina = True

if carro and (gasolina or edad >17):
    print('Puedes manejar')
