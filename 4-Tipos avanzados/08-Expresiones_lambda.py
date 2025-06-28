# en la clase anterior vimos como definimos una función para que la usemos dentro del metodo sort para ordenar la lista, pero puede ser una mala practica en el desarrollo. Para esto se usan las expresiones lambda, las cuales son llamadas
# tambien funciones fantasmas, ya que estas se escriben dentro de los parentesis del metodo, esto se hace en el argumento key del metodo sort. Pero la sintaxis de lambda es mucho mas corta y limpia, ya que omitimos la palabra def y la palabra return, 
# solo escribimos el nombre del parametro y seguido de dos puntos el valor de lo que debe retornar.
lista_avanz = [["Python", 3], ["Experto", 1], ["Diciembre", 11]]
lista_avanz.sort(key=lambda x: x[1])
print(lista_avanz)
