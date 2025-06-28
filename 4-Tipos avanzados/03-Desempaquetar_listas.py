# Podemos asignar variables para cada valor dentro de una lista y tambien podemos usar las variables con *, las cuales funcionaran como si fueran xargs, lo cual tomara a todos los elementos sin una variable y guardara a
#  todos esos elementos en una sola variable.
primero, segundo, tercero, *otros = list(range(11))
print(otros)
print(primero, segundo, tercero)

primero, *otros, ultimo = list(range(11))
print(ultimo)
