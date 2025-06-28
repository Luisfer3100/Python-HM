class Lista(list):
    def prepend(self, item):
        self.insert(0, item)

lista = Lista([1,2,3,4])
lista.prepend(0)
print(lista)
lista.prepend(5)
print(lista)
