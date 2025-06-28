lista_num = [3,1,5,7,4,3,6,8]

# sort
lista_num.sort() # Este metodo de listas, nos acomodara en orden los elementos de la lista. En este caso se hara con el ejemplo de una lista con numeros en orden
# aleatorio.
print(lista_num)

# sort reverse
lista_num.sort(reverse=True) # Tambien podemos ordenarlos de mayor a menor, usando el argumento reverse, al cual si le damos el valor de un booleano 'True', nos lo
# ordenara de mayor a menor.
print(lista_num)

# Sorted
numeros = [1,5,3,7,9,5,32,8]
numeros_nuevos = sorted(numeros) # Este metodo es muy similar al de sort, la diferencia es que sorted, crea una nueva lista. Por lo cual lo mejor es guardarla en
# una nueva variable
print(numeros)
print(numeros_nuevos)

# sorted reverse
numeros_nuevos = sorted(numeros, reverse=True) # Al igual que en sort, tambien podemos hacer uso del argumento reverse, para acomodarlos de mayor a menor.
print(numeros_nuevos)

# LISTAS AVANZADAS

# sort
lista_avanz = [[1, 'Python'],[4, 'Carro'], [3, 'Esternocleidomastoideo']] # En este caso, el metodo sort, tomara el primer elemento de cada lista dentro de la lista
# y de ese se guiara para acomodarlos.
lista_avanz.sort()
print(lista_avanz)
# Pero que pasaria si el numero se encuentra en otro indice de la lista que no sea el 0? Para esto creariamos una función que retorne el segundo elemento de las
# sublistas.
nueva_lista_avanzada = [['Python', 1],['Carro', 4], ['Esternocleidomastoideo', 3]]

def ordenar(elemento):
    return elemento[1] # Esta sera la funcion la cual retorne el indice 1 de cada sublista

nueva_lista_avanzada.sort(key=ordenar) # La palabra reservada key, es para indicar que usaremos una función dentro del metodo
print(nueva_lista_avanzada)

# sort reverse
nueva_lista_avanzada2 = [['Python', 5],['Carro',3], ['Esternocleidomastoideo', 8]]

def ordenar2(elemento):
    return elemento[1]

nueva_lista_avanzada2.sort(key=ordenar2, reverse=True) # En este caso tambien se puede hacer uso de reverse.
print(nueva_lista_avanzada2)

# ¡¡ A pesar de que se nos enseño esto, no es de lo practico, por lo cual en la siguiente sesion se nos enseñara sobre expresiones LAMBDA !!
