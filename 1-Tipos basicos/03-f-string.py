# Como se vio en la anterior clase, podemos concatenar los string y tambien podemos concatenar las variables, por ejemplo tener 2 variables que queremos concatenar para hacer un solo string:
cadena = 'Hola'
cadena2 = 'Mundo'
cadena3 = cadena + ' ' + cadena2
print(cadena3)

# Format-string (f-string) nos permite concatenar y hacer diversas sentencias en una sola linea de string, sin entrar y salir para concatenar. Para esto debemos de poner la f antes de las comilas:
cadena = 'Hola'
cadena2 = 'Mundo'
cadena3 = f'{cadena} {cadena2}'
print(cadena3)

# La gran ventaja de f-string es que no se necesita usar el signo de concatenación y se puede ejecutar todo tipo de sentencias dentro de las llaves:
cadena = 'Hola'
print(f'Estas son mis sentencias: {cadena} y {2+2}')
