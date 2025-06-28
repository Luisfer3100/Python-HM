datos = [1,2,3,4,4,5,]

def calcular_moda(dato):
    frecuencia = {}
    for n in dato:
        if n not in frecuencia:
            frecuencia[n] = 1
        else:
            frecuencia[n]+=1
    return max(frecuencia, key=frecuencia.get) # Aqui le indicamos a max() que tome como iterable a frecuencia, pero en lugar de que devuelva la clave mas grande
# le decimos con .get que devuelva la clave con el valor más alto

def calcular_mediana(dato):
    lista_ordenada = sorted(dato)
    largo = len(lista_ordenada)
    mitad = largo//2
    if largo%2==0:
        return (lista_ordenada[mitad-1] + lista_ordenada[mitad])/2
    else:
        return lista_ordenada[mitad]

print(calcular_moda(datos))
print(calcular_mediana(datos))