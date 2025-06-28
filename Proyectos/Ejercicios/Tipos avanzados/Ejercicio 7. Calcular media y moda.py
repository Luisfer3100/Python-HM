datos = [1,2,3,4,4,5,]

def calcular_mediana(dato):
    lista_ordenada = sorted(dato)
    n = len(lista_ordenada)
    mitad = n//2
    if n % 2 == 0: # Esto condiciona que si el largo de la lista, es igual a 0 el residuo, entoncesla lista es de total par, por lo cual se tomaran los 2 valores
        # del centro para la mediana.
        return (lista_ordenada[mitad-1] + lista_ordenada[mitad])/2 # aqui se indica que se tomara un elemento antes del indice el cual seria el valor de 'mitad'
    # y a este se le sumara al elemento del indice del valor de 'mitad' y esta suma entre 2 para sacar el promedio.
    else:
        return lista_ordenada[mitad]

def calcular_moda(dato):
    frecuencia = {}
    for n in dato:
        if n in frecuencia:
            frecuencia[n] +=1
        else:
            frecuencia[n] = 1
    return max(frecuencia, key=frecuencia.get)

mediana = calcular_mediana(datos)
moda = calcular_moda(datos)

print(f'''
La moda es: {moda}
Y la mediana es: {mediana}''')