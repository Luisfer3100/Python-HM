# Los Xargs son argumentos que se pasan a una función cuando no se conocen la cantidad de argumentos. Esto deja abierta la cantidad de argumentos que se podran pasar cuando se llame a la función.
# Para indicar que un parametro sera Xargs, se usa el simbolo de * antes del nombre del parametro:
def sumar(*numeros):
    total = 0
    for num in numeros:
        total = total +  num
    return total
print(sumar(1,5,4,8,16))
# En este ejemplo que use, podemos ver que solo indique elnjombre del parametro iniciando con *, lo cual indica que sera de tipo de xargs y podemos pasar tantos argumentos como queramos.