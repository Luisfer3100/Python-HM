# Controladores de flujo
edad = 58

if edad >= 70:
    print('Puede ver la pelicula con un super descuento.')
elif edad >= 55:
    print('Puede ver la pelicula con un descuento.')
elif edad >= 18:
    print('Puede ver la pelicula.')

# Mayor especificidad usando operadores lógicos
edad = 58

if edad >= 18 and edad <55:
    print('Puede ver la pelicula.')
elif edad >= 70:
    print('Puede ver la pelicula con un super descuento.')
elif edad >= 55 and edad <70:
    print('Puede ver la pelicula con un descuento.')
