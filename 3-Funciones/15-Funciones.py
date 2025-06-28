# funcion sin parametros
def saludo():
    print('Hola Mundo')

saludo()

# Funcion con parametros y entrada del usuario
nombre = input('¿Cual es tu nombre? ')

def saludo0(name):
    print(f'Hola, {name}')
    
saludo0(nombre)

# Sin pedirle entrada al usuario
def saludo1(name):
    print(f'Hola, {name}')
    
saludo1('Luis')
