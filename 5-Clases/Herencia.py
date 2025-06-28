class Humano:
    def __init__(self, nombre):
        self.nombre = nombre
    def comer(self):
        print(f'{self.nombre} esta comiendo.')


class Profesor(Humano):
    def ensenar(self):
        print(f'{self.nombre} esta enseñando.')


class Programador_profesor(Profesor):
    def programando(self):
        print(f'{self.nombre} esta programando.')

profe = Profesor('Luis')
profe.ensenar()

programador = Programador_profesor('Fernando')
programador.programando()
programador.ensenar()

profe.comer()
programador.comer()

