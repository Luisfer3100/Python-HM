# Pedir al usuario los 2 numeros:
num1 = int(input('Dame el primer numero de la operación: '))
num2 = int(input('Ahora dame el segundo: '))

# Ahora se hara el script para los mensajes y operaciones:
print(f'''Con los numeros {num1} y {num2}, los resultados son: \n
Suma de {num1} y {num2}: {num1+num2}
Resta de {num1} y {num2}: {num1-num2}
Multiplicación de {num1} y {num2}: {num1*num2}
División de {num1} y {num2}: {num1/num2}
''')
