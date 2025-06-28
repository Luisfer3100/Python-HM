# Crear una nueva lista a partir de 2 listas y entre estas añadir string.
l1 = [10,20]
l2 = [30,40]
l3 = [*l1, 'Hola', *l2, 'Mundo']
print(l3)

# Combinar diccionarios
info1 = {'nombre':'Luis', 'edad':24}
info2 = {'edad':25, 'correo':'luis@gmail.com'} # Esta edad quedara como la del valor
info_unida = {**info1, **info2}
print(info_unida)

# Diccionario con valores predeterminados
defaults = {'tema':'oscuro', 'idioma':'es'}
usuario = {'idioma':'en'}
print({**defaults, **usuario}) # No lo guarde en una variable, solo lo pase a imprimir
