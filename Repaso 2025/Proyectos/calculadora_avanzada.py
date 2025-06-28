num1 = int(input('Num 1: '))

while True:
    operacion = input('Operación: ')
    if operacion.lower() == 'salir':
        break

    num2 = int(input('Num 2: '))

    if operacion == '+':
        resultado = num1 + num2
        print(resultado)
        num1 = resultado
    elif operacion == '-':
        resultado = num1 - num2
        print(resultado)
        num1 = resultado
    elif operacion == '/':
        resultado = num1 / num2
        print(resultado)
        num1 = resultado
    elif operacion == '*':
        resultado = num1 * num2
        print(resultado)
        num1 = resultado
