# Objetivo: Crear una clase Libro que permita llevar el control de libros en una biblioteca.
class Libro:
    total_libros = 0
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.prestado = None
        Libro.total_libros +=1

    def marcar_prestado(self):
        self.prestado = True

    def devolver_libro(self):
        self.prestado = False
        return self.prestado

    def mostrar_info(self):
        return f'Titulo: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas} y el estado de prestado del libro es: {self.prestado}.'

    @classmethod
    def contar_libros(cls):
        return f'Se han creado {cls.total_libros} libros.'

l1 = Libro('Python', 'Fede', 213)
l1.marcar_prestado()
print(l1.mostrar_info())

l1.devolver_libro()
print(l1.mostrar_info())

l2 = Libro('La teoria del todo', 'S. Hawking', 459)
l2.marcar_prestado()
print(l2.mostrar_info())

l2.devolver_libro()
print(l2.mostrar_info())