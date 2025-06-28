usuario = {
    "id": 1,
    "nombre": "Luis",
    "ciudad": "Culiacán"

}

print(usuario["nombre"])

usuario["edad"] = 25
print(usuario)

del usuario["ciudad"]
print(usuario)

#usuario['lala'] = 12 #Descomentar para ver el resultado de cuando si se encuentra el elemento dentro del diccionario.
if 'lala' in usuario:
	print(usuario['lala'])

for n in usuario.items():
	print(n)

usuarios = [
    {'id': 1, "nombre": 'Luis'},
    {'id': 2, "nombre": 'Mara'},
    {'id': 3, "nombre": 'Raul'},
    {'id': 4, "nombre": 'Jorge'}
]

for n in usuarios:
    print(n['id'])
