class Humano:
    def comer(self):
        print('Esta comiendo.')

    def correr(self):
        print('Corre a 20km/h')


class Profesor:
    def ensenar(self):
        print('Esta enseñando.')

    def correr(self):
        print('Corre a 18km/h')


class Programador_profesor(Humano, Profesor):
    def programando(self):
        print('Esta programando.')

progrprof = Programador_profesor()
progrprof.correr()