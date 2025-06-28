# Primer nombre (obligatorio)
primer_nombre=input('Dame tu primer nombre: ').strip().capitalize()
while not primer_nombre:
    print('Es necesario tu primer nombre.')
    primer_nombre=input('Dame tu primer nombre: ').strip().capitalize()

# Segundo nombre (opcional)
segundo_nombre=input('Ahora tu segundo nombre: ').strip().capitalize()

# Primer apellido (Obligatorio)
primer_apellido=input('Dame tu primer apellido: ').strip().capitalize()
while not primer_apellido:
    print('Es necesario tu primer apellido.')
    primer_apellido=input('Dame tu primer apellido: ').strip().capitalize()

# Segundo nombre (opcional)
segundo_apellido=input('Ahora tu segundo apellido: ').strip().capitalize()

# Crear nombre completo
nombre_completo = f'{primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido}'.replace('  ', ' ')

print(f'Tu nombre completo es: {nombre_completo}')
