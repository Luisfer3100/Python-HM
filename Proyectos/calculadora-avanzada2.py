print('''Bienvenidos a la calculadora avanzda.
Para salir escribe "salir"
Las operaciones son: suma, resta, multi y div.''')

num1 = int(input('Ingrese un numero: '))
while True:
    op = input('Indicame que operacion deseas: ').lower()
    if op == 'salir':
        print('Saliste de la calculadora avanzada.')
        break
    num2 = int(input('Dame el siguiente numero: '))

    if op == 'suma':
        num1 += num2
    elif op == 'resta':
        num1 -= num2
    elif op == 'multi':
        num1 *= num2
    elif op == 'div':
        num1 /= num2
    else:
        print('La operación no existe.')
    
    print(num1)
