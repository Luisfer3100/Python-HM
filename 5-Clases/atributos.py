class Perro:
    patas = 4

    def __init__(self, nombre):
        self.nombre = nombre

    def presentar_perro(self):
        print(f'{self.nombre} tiene {self.patas} patas.')


mi_perro = Perro('Toby')
mi_perro2 = Perro('Muñeca')
mi_perro.presentar_perro()  # Toby tiene 4 patas.
mi_perro2.patas = 3
mi_perro2.presentar_perro()