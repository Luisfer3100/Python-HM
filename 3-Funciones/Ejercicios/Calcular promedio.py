# Definir la función
def calcular_promedio(*num):
    if not num:
        return 0
    else:
        total = 0
        for n in num:
            total += n
        return total/len(num)

print(calcular_promedio(1,2,3,4,5))
