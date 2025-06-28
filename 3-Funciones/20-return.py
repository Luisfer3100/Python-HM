# La palabra reservada "return" es utilizada para terminar la ejecución de una función y devolver un valor. Esto se usa para que la funcion pueda regresar un valor al programa principal.
def suma(a, b):
    saludo = "Hola Mundo"
    return a + b

c = suma(3, 4)
d = suma(c, 6)
print(d)
