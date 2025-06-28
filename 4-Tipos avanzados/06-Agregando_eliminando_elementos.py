# para  agregar un elemento a la lista, podemos usar insert, el cual requiere dos argumentos: el índice donde se agregara y el elemento a insertar.
frutas = ['banana', 'apple', 'kiwi', 'grape']
frutas.insert(2, 'mango')
print(frutas)

# con el metodo insert podemos agregar un elemento en la posición final sin saber su índice, esto lo hacemos con el indice negativo:
frutas1 = ['banana', 'apple', 'kiwi', 'grape']
frutas1.insert(-1,'mango')
print(frutas1)

# Tambien podemos usar otro metodo para agregar u elemento al final de la lista, seria con append: 
frutas2 = ['banana', 'apple', 'kiwi', 'grape']
frutas2.append('mango')
print(frutas2)

# ahora eliminaremos elemento de las listas, para esto usaremos como primer elemento el de remove, este nos eliminara un elemento, indicando el valor del elemento:
frutas3 = ["banana", "apple", "kiwi", "grape", "banana"]
frutas3.remove("apple")
print(frutas3)

# al igual que con los metodos para añadir elementos, tambien hay un metodo para eliminar el ultimo elemento de la lista, seria con pop:
frutas4 = ["banana", "apple", "kiwi", "grape"]
frutas4.pop()
print(frutas4)

# tenemos la palabra reservada del, esta tiene una sintaxis un poco diferente, esta eliminara el elemento que le pasemos dentro de los parentesis de dicha lista:
frutas5 = ["banana", "apple", "kiwi", "grape"]
del frutas5[2]
print(frutas5)

# por ultimo tenemos el metodo clear, el cual como su nombre lo indica, limpia la lista:
frutas6 = ["banana", "apple", "kiwi", "grape"]
frutas6.clear()
print(frutas6)
