# Si nosotros definimos una función al inicio de nuestro programa y resulta que nuestro programa se esta volviendo demasiado largo y al fianl del programa llamamos a la función, pero no nos acordamos como era el orden de los argumentos
# los podemos nombrar lo cual es poner el nombre del parametro de la funcion y seguido de un signo de igual, el valor que le daremos:

def saludo(nombre, apellido):
    print(f'Hola, {nombre} {apellido}')

saludo(apellido='Osuna', nombre='Luis') # A pesar de que los valores de los argumentos no estan en orden, al nombrar los arguemtnos y despues darles su valor, la funcion acomoda como corresponde esos valores.
