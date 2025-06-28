mascotas = ["Muñeca", "Toby", "Bodoque", "Coco", "Snoopy", "Bolt"]
# Podemos acceder a un solo elemento de la lista, con los crchetes para acceder a los indices de estos elementos.
print(mascotas[2])
# Tambien podemos acceder mediante indices negativos, que comienzan desde el final de la lista.
print(mascotas[-2])
# Podemos cambiar el valor de un elemento de la lista.
mascotas[3] = "Puppy"
print(mascotas)
# Revanar la lista
print(mascotas[1:4])
# Podemos controlar cada cuantos elementos agregara al rebanado, esto se hace con un tercer numero en el rebanado
print(mascotas[::2])

# Tambien lo podriamos hacer con un rango de numeros
numeros = list(range(21))
print(numeros[::2]) # Este nos dara los numeros pares del rango
print(numeros[1::2]) # Este nos dara los numeros impares del rango
