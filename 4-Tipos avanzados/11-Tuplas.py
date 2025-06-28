# Es una colección de datos inmutables, son utiles cuando una colección de datos queremos que se mantenga igual, con cambios.

# Las tuplas usan parentesis en su sintaxis. Este seria una tupla vacia:
tupla = ()

# También podemos definir una tupla sin necesidad de los parentesis pero no es lo mas recomendable:
tupla_num = 1,2,3,4,5
print(type(tupla_num))

# Si queremos crear una tupla con un solo elemento lo que se debe hacer es pasarle una coma despues del elemento
tupla_uno = (1,)
print(tupla_uno)

# No podemos modificar las tuplas pero si podemos acceder a elementos de ella y concatenar tuplas:
tupla_num_dos = tupla_num[1]
print(tupla_num_dos)

tupla_abc = ('a','b','c')
tupla_mixta = tupla_num + tupla_abc
print(tupla_mixta)

# Y como lo dije al principio, podemos usar una tupla cuando una colección la queramos mantener inmutable. Para esto usare el ejemplo de que una lista de nuestro
# código la queremos convertir a tupla, para asi hacerla inmutable:
lista = [[1,2], ['a','b'], [3,4], ['c','d']]
lista_a_tupla = tuple(lista)
print(lista_a_tupla)

# Podemos desempaquetar las tuplas para asi tener variables con valor de algunos elementos de la tupla:
a, b, c, d, *otros = tupla_mixta
print(a, b, c,d,otros)

# Los metodos de las tuplas, son index y count
print(tupla_mixta.index('a'))

tupla_dos = (1,2,3,3,4,5)
print(tupla_dos.count(3))
