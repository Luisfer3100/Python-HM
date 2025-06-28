# En clases pasadas vimos que los argumentos seran el valor real que le daremos a la función cuando la llamemos, y los parametros son las variables temporales internas en la función. Los argumentos seran valores dados por el usuario o en algunos
# casos por nosotros los desarrolladores. Pero que pasaria si el usuario no quiere dar el valor de un argumento y corre el programa sin el valor? Para eso podemos definir por defecto un valor:

def saludo(name='Usuario'):
    print(f'Hola, {name}')

saludo()

# Asi se veria si no le pasamos el argumento a la llamada de la función. Y si le pasamos el valor seria asi:
saludo('Luis')
