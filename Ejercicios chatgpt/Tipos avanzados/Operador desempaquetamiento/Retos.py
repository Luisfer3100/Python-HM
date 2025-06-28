# Reto1. Tenemos dos listas con nombres de usuarios. Algunos están repetidos. Combinemos las listas y elimina duplicados.
usuarios1 = ['Luis', 'Ana', 'Carlos']
usuarios2 = ['Ana', 'Maria', 'Luis', 'Pedro']

usuarios0 = [*usuarios1, *usuarios2]
usuarios0 = set(usuarios0)
usuarios0 = sorted(usuarios0) # Este ordena alfabeticamente o de menor a mayor, ya sea en caso de numeros
print(usuarios0)

# Reto 2. Configuración final del usuario. Combina configuraciones por defecto y perzonalizadas de un usuario.
por_defecto = {'tema':'claro', 'idioma':'en', 'notificaciones':True}
por_usuario = {'tema':'oscuro', 'idioma':'es', 'notificaciones':True}
confi_final = {**por_defecto, **por_usuario}
print(confi_final)

# Reto 3. Crear una función flexible con *args y **kwargs (desempaquetamiento en funciones).
# Crear una función mostrar_info que reciba cualquier número de argmentos y cualquier número de claves y valores.
def mostrar_info(*args,**kwargs):
    print(f'Valores posicionados: {args}')
    print(f'Valores con clave:')
    for clave, valor in kwargs.items():
        print(f'{clave}:{valor}')

mostrar_info('Luis', 'osuna', 31, telefono='iPhone', laptop='macbook') # aqui los kwargs no se ubican dentro de llaves y no lleva comillas
# las key. Tampoco se usa los dos puntos, si no que el signo igual.

# Reto 4. Registrar multiples compras(*args). Crear una función registrar_compras que reciba cualquier cantidad de productos comprados (nombres de productos como
# string) y que: Imprima cada producto comprado. Imprima cuántos productos se compraron en total.
def registrar_compras(*args):
    productos = []
    for n in args:
        productos.append(n)

    for n in productos:
        print(f'Producto: {n}')
    print(f'En total son {len(productos)} productos.')

registrar_compras('Arroz','Leche','Pan','Canela')

# Reto 5. Crear un perfil de usuario. Para esto crearemos una función crear_perfil(**kwargs) que reciba datos como nombre, edad, ciudad, etc. Y que imprima cada dato
# con su nombre(key). Si algún dato no se incluye, ignóralo (es flexible).
def crear_perfil(**args):
    for clave, valor in args.items():
        print(f'{clave}:{valor}')

crear_perfil(nombre='Luis', edad=25, ocupacion='Programador')

# Reto 6. Combinar múltiples listas sin duplicados. Crea una función combinar_usuarios(*listas) que reciba cualquier cantidad de listas de usuarios y combine todos
# los usuarios, elimine duplicados, ordene la lista final alfabéticamente y la regrese como resultado.
l1 = ["Luis", "Ana"]
l2 = ["Carlos", "Luis"]
l3 = ["Pedro", "Ana"]

def combinar_usuarios(*listas):
    lista_nueva = []
    for n in listas:
        lista_nueva.extend(n)
    lista_nueva=sorted(lista_nueva)
    lista_nueva=set(lista_nueva)
    print(lista_nueva)

combinar_usuarios(l1,l2,l3)

# RETO FINAL. Sistema de registro y reporte de usuarios.
# Crear un sistema que permita: Registrar usuarios con datos como nombre, edad, ciudad, ocupacion, etc. Aceptar multiples usuarios a la vez usando *args **kwargs.
# Guardar todos los usuarios en una lista de diccionarios. Imprimir un reporte ordenado alfabéticamente por nombre. Imprimir cuantos usuarios hay y su edad promedio.
usuarios = []

def registrar_usuarios(*args):
    for n in args:
        usuarios.append(n)

def mostrar_reporte():
    if not usuarios:
        print('No hay usuarios registrados.')
        return

