# Objetivo: Crear una clase Estudiante que permite registrar estudiantes en una escuela, calcular su promedio y controlar cuantos estudiantes se han creado.
class Estudiante:
    escuela = 'Escuela Python'
    total_estudiantes = 0

    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
        Estudiante.total_estudiantes += 1

    def promedio(self):
        promedio_total = 0
        for cali in self.calificacion:
            promedio_total+=cali
        resultado = promedio_total // len(self.calificacion)
        self.calificacion = resultado
        return self.calificacion

    def mostrar_info(self):
        return f'{self.nombre}, {self.calificacion}, {self.escuela}'

    @classmethod
    def cambiar_escuela(cls, nombre_escuela):
        cls.escuela = nombre_escuela

    @classmethod
    def contar_estudiantes(cls):
        return cls.total_estudiantes

e1 = Estudiante('Luis', [10,9,9])
e2 = Estudiante('Mara', [10,9,10])

print(e1.promedio())
print(e2.promedio())

print(e1.mostrar_info())
print(e2.mostrar_info())

print(Estudiante.contar_estudiantes())

