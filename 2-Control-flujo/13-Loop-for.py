# Los loops for tienen muchas utilidades dentro de python. Pero en esta clase se toco el tema de iterar elementos. Por ejemplo los caracteres de un string:
cadena = 'hola'

for elemento in cadena:
    print(elemento)

# No solo se puede iterar cadenas, tambien se puede iterar un rango de numeros y muchos mas tipos de datos: (en la funcion range() solo se incluira hasta un
# número antes del indicado)
for i in range(7):
    print(i)

# Incluso en este loop for podemos utlizar una estructura de control if-else para hacer decisiones:
buscar  =  4
for i in range(4):
    if i == buscar:
        print(f'El numero {buscar} esta en el rango.')
        break
else:
    print(f'El numero {buscar} no esta en el rango.')
        