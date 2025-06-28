# Sintaxis
cadena = 'Hola Mundo'

# Concatenación
cadena = 'Hola' + 'Mundo' # Esta sentencia nos pintara los string sin un espacio entre ellos, por lo cual deberemos concatenar el espacio en blanco .
print(cadena)
# Concatenacion con espacio en blanco
cadena = 'Hola' + ' ' + 'Mundo' # Otra forma seria darle un espacio en blanco en el string de Hola ('Hola ') o en el string de Mundo (' Mundo')
print(cadena)

# len
print(len(cadena))

# Indice
print(cadena[3]) # Nos pintara el indice 3 de nuestra variable. Recordar que los indices tienen como base el numero 0 asi que nuestro primer caracter tendria el indice numero 0
print(cadena[-1]) # También podemos navegar por los indices de forma negativa, por lo cual al indicar que queremos acceder al indice -1, nos retorno el ultimo caracter del string, si es -2 seria el penultimo y asi # consecutivamente.

# Con los indices podemos rebanar los string. Por ejemplo si de la cadena 'Hola mundo' queremos extraer la subcadena 'Hola', se haria con los indices correspondientes:
sub_cadena = cadena[0:4]
print(sub_cadena)

# Si el rebanado que queremos hacer es desde cierto indice hasta el indice final y no sabemos el numero del indice final, podemos omitir el indicar el numero de indice final y python tomara como defecto que queremos rebanar hasta el final del string:
sub_cadena = cadena[5:]
print(sub_cadena)

# En el caso de omitir el indice de inicio, rebanara por defecto desde el indice 0:
sub_cadena = cadena[:4]
print(sub_cadena)

# Otra forma de rebanar que seria un poco absurda es no pasar ninguno de los 2 indices y esto haria que rebane desde el indice 0 hasta el indice final. Digo un poco absurdo por que el resultado seria como si no hubiera rebanado:
sub_cadena = cadena[:]
print(sub_cadena)
