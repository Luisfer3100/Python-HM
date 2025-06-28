# Los set son un tipo de colección, en el cual no se pueden repetir elementos y no estan ordenados.Si tenemos un elemento duplicado, el set lo eliminara.
# La sintaxis de los set, son en llaves {} o se puede usar la función set(), para crear un set:
set_uno = {1,2,3,3,4,5}
lista = [1,2,3,3,4,5]
set_dos = set(lista)
print(set_uno, set_dos)

# En los set, tenemos operaciones con las cuales podemos crear un nuevo set a partir de dos set:
# Union, esta unira ambas tuplas, eliminando duplicados (el operador es |):
set_num_uno = {1,2,3}
set_num_dos = {3,4,5}
set_num_tres = set_num_uno|set_num_dos
print(set_num_tres)

# Intersección lo que hara es solo retornar el elemento que este presente en ambos set:
set_num_cuatro = set_num_uno&set_num_dos
print(set_num_cuatro)

# Diferencia lo que retornara sera solo los elementos que se encuentren en el primer set, pero sin mostrar algun elemento de su set que se encuentre en el segundo set:
set_num_cinco = set_num_uno-set_num_dos # Este se entiende como set_num_uno menos los elementos que se encuentren en el set_num_dos
print(set_num_cinco)

# Diferencia simetrica es lo contrario, esta retorna de ambos set, pero sin retornar el elemento que este en ambos set:
set_num_seis = set_num_uno^set_num_dos
print(set_num_seis)
