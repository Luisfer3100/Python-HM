frutas = ["manzana", "pera", "naranja", "melon"]
for fruta in frutas:
    print(fruta)

# Enumerar los elementos de una lista con su indice. Función enumerate() lo cual regresa tuplas:
for fruta in enumerate(frutas):
    print(fruta)

# Si queremos acceder a los elemento de esas tuplas por separado debemos de indicar los elementos a recorrer en el loop:
for indice, fruta in enumerate(frutas):
    print(indice, fruta) # Al ejecutarlo podremos ver que ya no se imprime como tuplas.

# Si le pasamos uno de los elementos a recorrer entonces solo imprimira ese elemento.
for indice, fruta in enumerate(frutas):
    print(fruta)

# También podriamos hacer este recorrido con los indices:
for fruta in enumerate(frutas):
    print(fruta[1])
