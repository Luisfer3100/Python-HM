# Objetivo: Crear una clase Alumno que almacene el nombre del alumno y sus calificaciones en diferentes materias, usando diccionarios y listas, y permita
# calcular promedios.
class Alumno:
    total_alumnos = 0
    def __init__(self, nombre, materias):
        self.nombre = nombre
        self.materias = materias
        Alumno.total_alumnos+=1

    def agregar_materia(self, nombre_materia):
        self.materias[nombre_materia] = []

    def agregar_calificacion(self, materia, calificacion):
        self.materias[materia].append(calificacion)

    def promedio_materia(self, materia):
        promedio = 0
        for cali in self.materias[materia]:
            promedio += cali
        return promedio/len(self.materias[materia])

    def promedio_general(self):
        suma = 0
        promedio = 0
        for n in self.materias.values():
            promedio += sum(n)
            suma += len(n)
        return promedio/suma

    def mostrar_info(self):
        print(f'El alumno {self.nombre} tiene estas materias:')
        for n, i in self.materias.items():
            print(n, i)
        print(f'Su promedio general es de: {self.promedio_general()}')

    @classmethod
    def contar_alumnos(cls):
        return cls.total_alumnos



diccio = {'español':[9,8], 'matematicas':[9,7]}
a1 = Alumno('Luis', diccio)
a1.agregar_materia('historia')
a1.agregar_calificacion('historia',7)
a1.agregar_calificacion('historia',8)
print(a1.promedio_materia('historia'))
print(a1.promedio_general())
a1.mostrar_info()
