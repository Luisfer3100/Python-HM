class Libro:
    total_libros = 0

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas
        Libro.total_libros+=1

    @property
    def titulo(self):
        return self.__titulo

    def __str__(self):
        return f'{self.__titulo} de {self.__autor}'

    def __len__(self):
        return self.__paginas

    def __eq__(self, other):
        if (self.__autor and self.__titulo) == (other.__autor and other.__titulo):
            return 'Son el mismo libro.'
        else:
            return 'No son el mismo libro.'

    @classmethod
    def contar_libros(cls):
        return cls.total_libros

class Persona:
    def __init__(self,nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return f'Nombre: {self.__nombre} - Edad: {self.edad} años.'

    def __eq__(self, other):
        if self.edad == other.edad:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.edad < other.edad:
            return True
        else:
            return False

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.__matricula = matricula

    def presentarse(self):
        return f'Nombre: {self.nombre} - Matricula: {self.__matricula}'

class Biblioteca:
    def __init__(self):
        self.__libros = []

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def mostrar_libros(self):
        for libro in self.__libros:
            print(libro)

    def __len__(self):
        return len(self.__libros)

    def __del__(self):
        return f'La biblioteca se ha eliminado.'

libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 98)
libro2 = Libro("1984", "George Orwell", 328)
libro3 = Libro("El principito", "Antoine de Saint-Exupéry", 98)

print(libro1 == libro3)  # True
print(len(libro2))       # 328
print(libro1)            # El principito de Antoine de Saint-Exupéry

print(Libro.contar_libros())  # 3

est = Estudiante("Luis", 20, "A12345")
est.presentarse()  # Soy Luis y mi matrícula es A12345

biblio = Biblioteca()
biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)
biblio.mostrar_libros()

print(len(biblio))  # 2
del biblio  # se llama al destructor