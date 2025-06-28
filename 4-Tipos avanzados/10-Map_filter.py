# map y filter son funciones integradas de python que permiten realizar operaciones sobre cada elemento de una lista.
# map nos ayudara a aplicar funciones a cada elemento de un iterable y devolver un nuevo iterable con los resultados.
def cuadrado(x):
    return x*x
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(cuadrado, numeros))
print(cuadrados)
# tambien podemos usar las funciones lambda para simplificar el codigo
numeros1 = [6, 7, 8, 9, 10]
cuadrados1 = list(map(lambda x: x*x, numeros1))
print(cuadrados1)

# filter nos ayudara a seleccionar solo los elementos que cumplan una condicion.
def par(x):
    return x%2==0
numeros2 = [1,2,3,4,5]
resultado = list(filter(par, numeros2))
print(resultado)
# y con expresiones lambda seria:
numeros3 = [6,7,8,9,10]
resultado1 = list(filter(lambda x:x%2==0, numeros3))
print(resultado1)
