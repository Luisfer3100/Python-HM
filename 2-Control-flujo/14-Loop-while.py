# Otro loop dentro de python es el while loop. Este loop, como su nombre lo dice, se ejecuta mientras la condicion se cumpla. Por ejemplo, que si un numero sea mayor a 10:

numero = 15

while numero > 10:
    print(numero)
    numero -=1
print('Se termino el loop.')
# Como variable inicial tenemos el numero 15 y en la condicion del while sentenciamos que mientras que numero sea mayor a 10 se imprimira el numero dentro de la variable y para que este loop no sea infinito, por cada vuelta al loop se restara 1 al 
# numero. Y fuera de la indentacion de el while tenemos la sentencia de print, la cual nos indica el fin del loop.

# Tambien podriamos poner el ejemplo de un loop en el cual el usuario estara ingresando un texto y este se pinte en pantalla hasta que ingrese el texto 'salir'. Para esto se inicializara una variable con string vacio y dentro del loop se reutilizara
# esta variable pero con una entrada input:
entrada = ' '
while entrada != 'salir':
    entrada = input('Ingrese un texto: ')
    if entrada!= 'salir':
        print(entrada)
print('Se termino el loop.')

# Debemos de tener en cuenta que los strings son sensibles a mayusculas y minusculas, por lo tanto 'Salir' y 'salir' no seran lo mismo para python. Para solucionar esto se recomienda usar la metodo lower() en la variable entrada:
entrada = ' '
while entrada.lower()!= 'salir':
    entrada = input('Ingrese un texto: ').lower()
    if entrada!= 'salir':
        print(entrada)
print('Se termino el loop.')

# En los ejemplos anteriores le hemos dado una condicion al loop while, en cual mientras la condicion sea verdadera se ejecute. Pero si hacemos un loop infinito, ¿Comó lo detenemos? Un loop infinito tiene la siguiente estructura:
# while True:
#     print('Loop infinito')
# Si le quitamos los simbolos de comentario, este loop se ejecutara infinitamente por que la condicion es siempre verdadera. Pero si dentro del loop podemos un 'break', este terminara el loop al cumplir una condicion que indicaremos 
# dentro de un control de flujo.
entrada = ' '
while True:
    entrada = input('Ingrese un texto: ').lower()
    if entrada != 'salir':
        print(entrada)
    else:
        print('Se termino el loop.')
        break
