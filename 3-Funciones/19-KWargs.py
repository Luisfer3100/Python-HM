# Este al igual que los xargs, es un parametro que permite pasar una cantidad variable de argumentos a una función. Lo que cambia es que en lugar de usar un * se utilizan 2 y al pasar los argumentos debemos hacerlo con la clave del valor, al igual 
# que los diccionarios, lo cual quiere decir que se debe de pasar el nombre del parametro seguido de un signo de igual y el valor.
def producto(**lista):
    print(lista)
producto(tele="Apple TV", celular="iPhone", tablet="iPad") # Si ejecutamos este codigo, podremos ver en consola que nos regresara estos argumentos pero con la sintaxis de un diccionario. Esto por que los KWargs son, KeyWords lo cual es la sintaxis
# de un diccionario en Python. Si nosotros queremos acceder solo a un valor de estas palabras clave, debemos indicarlo dentro de la funcion con el simblo de corchetes([simbolo de indice]), indicando el nombre de la palabra clave que deseamos obtener.
def producto0(**lista):
    print(lista["celular"])
producto0(tele="Apple TV", celular="iPhone", tablet="iPad") # Ahora si ejecutamos este codigo, podremos ver en consola que nos regresara el valor de 'celular'.
