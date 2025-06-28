# lista = [["Chanchito", 3], ["Toby", 5], ["Mar", 2]]
# nombres = [usuario[0] for usuario in lista]
# print(nombres)

lista = [["Chanchito", 3], ["Toby", 5], ["Mar", 2]]
nombres = [usuario[0] for usuario in lista if usuario[1] > 2]
print(nombres)
