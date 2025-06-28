# para ordenar una lista, modificandola en el mismo "lugar", usaremos el metodo sort y si queremos ordenar la lista
# pero que cree una nueva lista con dicho resultado, entonces usaremos la función sorted():
numeros = [5, 2, 8, 1, 9, 3]
numeros.sort()
print(numeros)
numeros_ord = sorted(numeros)
print(numeros_ord)

# si quisieramos que el orden fuera inverso, es decir del mayor al menor, tanto en la funcion sorted como en el metodo sort,
# podemos usar el argumento reverse:
numeros.sort(reverse=True)
print(numeros)
numeros_ord_r = sorted(numeros, reverse=True)
print(numeros_ord_r)

# estos incluso pueden servir en matriz:
lista_avanzada = [[4, "Mono"], [2, "Carro"], [9, "Cielo"]]
lista_avanzada.sort()
print(lista_avanzada)
lista_avanzada_or = sorted(lista_avanzada)
print(lista_avanzada_or)

# pero si el elemento de los numeros, se encuentra en otro indice detro de la lista que no sea igual a 0, los elementos no se
# ordenaran del numero mas chico al mas grande, si no que por abecedario:
lista_avanzada = [["Mono", 4], ["Carro", 2], ["Cielo", 9]]
lista_avanzada.sort()
print(lista_avanzada)
lista_avanzada_or = sorted(lista_avanzada)
print(lista_avanzada_or)

# la "solución" a esto seria crear una función para que el elemento que se retorne para evaluar y ordenar sea el elemento donde
# se encuentren los numeros:
lista_avanz = [["Python", 3], ["Experto", 1], ["Diciembre", 11]]

def ordenar(elemento):
    return elemento[1]

lista_avanz.sort(key=ordenar)
print(lista_avanz)

# Argumento key y reverse
lista_avanz = [["Python", 3], ["Experto", 1], ["Diciembre", 11]]

def ordenar1(elemento):
    return elemento[1]

lista_avanz.sort(key=ordenar1, reverse=True)
print(lista_avanz)
